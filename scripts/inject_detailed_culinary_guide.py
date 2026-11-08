# -*- coding: utf-8 -*-
"""
Script to:
1. Remove all specific personal names of PICs ("Pak Yudi, Ikbal", "Rizal", "Bu Ricky", "Bu Linda", "Faiz", "Abidin")
   and replace them with formal functional team station names.
2. Inject the complete, detailed step-by-step culinary & bumbu guide for kitchen volunteers
   into the Station Directives, Subtabs, Fullscreen Reader, and Menu Item Cards.
"""

import os
import re

print("Starting injection of detailed culinary guide and removal of PIC names...")
