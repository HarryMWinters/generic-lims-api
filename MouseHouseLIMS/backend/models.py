from django.db import models

from .models import (dna_extraction, electrophoresis,
                     gel_image, master_mix, mouse, pcr_reaction, tissue_sample)

"""
Mouse -> 
Tissue Sample ->
DNA Extraction ->
+ Master Miz ->
PCR Reaction -> 
Electrophoresis ->
Gel Image 
"""
