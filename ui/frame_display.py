from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
import os
import imageio
import sys
import numpy as np
from qimage2ndarray import array2qimage


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self):
        self.setObjectName("Form")
        self.setWindowTitle('Noise2Noise Video Restoration Reader Study')
        self.methods = ['original', 'gt', 'n2n_eps0.1']
        self.frames = ['previous', 'current', 'next']
        self.permutation = np.random.permutation(3)
        self._setup_constants()
        self._load_frames()
        self._setup_labels()
        self._setup_buttons()
        self._setup_frame_update_timer()
        self.resize(3 * self.frame_width + 4 * self.padding,
                    self.frame_height + 150)

    def _setup_frame_update_timer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.next_frame)
        self.timer.start(self.ms_per_frame)

    def _setup_constants(self):
        self.button_width = 101
        self.button_height = 51
        self.button_spacing = 120
        self.button_yoff = 540
        self.button_xoff = 100

        self.frame_width = 512
        self.frame_height = 512
        self.padding = 20

        self.current_sample = 0
        self.current_frame_idx = 0
        self.frame_diff = +1
        self.ms_per_frame = 100

        self.ratings = np.zeros((3, 3))

    def _setup_labels(self):
        self.labels = []
        for i_method in self.permutation:
            label = QtWidgets.QLabel(self)
            label.setGeometry(QtCore.QRect(
                self.padding + i_method * (self.padding + self.frame_width),
                self.padding,
                self.frame_width,
                self.frame_height))
            self.labels.append(label)

    def _setup_buttons(self):
        self.button_texts = ['Overall\nBest',
                             'Least\nFlickering',
                             'Significant\nSmoothing']
        self.buttons = []
        for i_method in self.permutation:
            buttons_for_method = []
            for i_button, text in enumerate(self.button_texts):
                button = QtWidgets.QPushButton(self)
                button.setCheckable(True)
                button.setGeometry(QtCore.QRect(
                    self.button_xoff + self.padding
                    + i_button * self.button_spacing
                    + i_method * (self.padding + self.frame_width),
                    self.button_yoff,
                    self.button_width,
                    self.button_height))
                button.setText(text)
                buttons_for_method.append(button)
            self.buttons.append(buttons_for_method)

        self.next = QtWidgets.QPushButton(self)
        self.next.pressed.connect(self.try_advance)
        self.next.setGeometry(QtCore.QRect(1500, 600, 100, 50))
        self.next.setText('Next')

    def _load_frames(self):
        num_samples = 8
        self.pixmaps = np.empty(
            (num_samples, len(self.methods), len(self.frames)), dtype=QPixmap)
        for sample in range(num_samples):
            for i_method, method in enumerate(self.methods):
                for i_frame, _ in enumerate(self.frames):
                    image_np = imageio.imread(
                        self.frame_path(i_method, sample, i_frame)
                        ).astype(np.float64) / 255
                    if method == 'n2n':
                        noise = 0.015 * np.random.randn(*image_np.shape)
                    else:
                        noise = np.zeros(image_np.shape)
                    self.pixmaps[sample, i_method, i_frame] = \
                        QPixmap.fromImage(array2qimage((
                            np.clip(image_np + noise, 0, 1) * 255
                        ).astype(np.uint8)))

    def _correct_button_configuration(self):
        sums_in_button = [0, 0, 0]
        for i_method, button_list in enumerate(self.buttons):
            sum_in_method = 0
            for i_button, button in enumerate(button_list):
                if button.isChecked():
                    sum_in_method += 1
                    sums_in_button[i_button] += 1
            if sum_in_method > 3:
                return False
        if sums_in_button[0] != 1:
            return False
        if sums_in_button[1] != 1:
            return False
        if sums_in_button[1] > 1:
            return False
        return True

    def _update_ratings(self):
        for i_actual, i_method in enumerate(self.permutation):
            button_list = self.buttons[i_actual]
            for i_button, button in enumerate(button_list):
                if button.isChecked():
                    self.ratings[i_method, i_button] += 1

    def _write_ratings(self):
        rating_path = './ratings'
        num_records = len(os.listdir(rating_path))
        np.save(os.path.join(rating_path, 'rating_' + str(num_records + 1)),
                self.ratings)

    def _closing_routine(self):
        self._write_ratings()
        self.close()

    def _reset_buttons(self):
        for buttons in self.buttons:
            for button in buttons:
                button.setChecked(False)

    def try_advance(self):
        if not self._correct_button_configuration():
            return

        self._update_ratings()
        self._reset_buttons()

        if self.current_sample == 7:
            return self._closing_routine()

        self.permutation = np.random.permutation(3)
        self.current_sample += 1

    def button_cb(self):
        sender = self.sender()
        for i_method, button_list in enumerate(self.buttons):
            if sender in button_list:
                print(i_method, self.button_texts[button_list.index(sender)])

    def frame_path(self, i_method, i_sample, i_frame):
        return os.path.join('../gif/', self.methods[i_method],
                            str(i_sample), self.frames[i_frame] + '.png')

    def next_frame(self):
        if self.current_frame_idx == 2:
            self.frame_diff = -1
        elif self.current_frame_idx == 0:
            self.frame_diff = +1
        self.current_frame_idx += self.frame_diff
        for i_label, i_method in enumerate(self.permutation):
            self.labels[i_label].setPixmap(self.pixmaps[
                self.current_sample, i_method, self.current_frame_idx])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
