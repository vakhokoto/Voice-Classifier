# from docx import Document
# import PyPDF2
# from docx.shared import Inches, Pt
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# document = Document()
# header = document.sections[0].header
# htable=header.add_table(1, 2, Inches(6))
# htab_cells=htable.rows[0].cells
# ht0=htab_cells[0].add_paragraph()
# kh=ht0.add_run()
# kh.add_picture('cover.jpg', width=Inches(1))
# ht1=htab_cells[1].add_paragraph('put your header text here')
# ht1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
# document.save('yourdoc.docx')

# Signal Generation
# matplotlib inline

from maracas.dataset import Dataset
import numpy as np
from scikits.audiolab import wavread, wavwrite
# from numba import autojit

# Make sure this is reproducible
np.random.seed(42)

d = Dataset()

# All files can be added one by one or by folder. Adding a folder will add
# all speech files inside that folder recursively if recursive=True.
d.add_speech_files('/home/vakhokoto/ML-Assignments/Voice-Classifier/Data/1/', recursive=True)

# When adding noises, you can give a "nickname" to each noise file. If you do not
# give it a name, the name will be the file name without the '.wav' extension
d.add_noise_files('/home/vakhokoto/ML-Assignments/Voice-Classifier/Data/1/devi-khos-1.wav', name='restaurant')
d.add_noise_files('/home/vakhokoto/ML-Assignments/Voice-Classifier/Data/1/devi-khos-1.wav', name='cafeteria')
d.add_noise_files('/home/vakhokoto/ML-Assignments/Voice-Classifier/Data/1/devi-khos-1.wav', name='traffic')

# Adding reverb files works like adding noise files
d.add_reverb_files('/home/vakhokoto/ML-Assignments/Voice-Classifier/Data/1/devi-khos-1.wav')
d.add_reverb_files('/home/vakhokoto/ML-Assignments/Voice-Classifier/Data/1/devi-khos-1.wav')

# When generating a dataset, you can choose which SNRs will be used and how many
# files per condition you want to be generated. 
d.generate_dataset([-6, -3, 0, 3, 6], 'Data/', files_per_condition=5)