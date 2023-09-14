# Copyright 2023 The Google Earth Engine Community Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START earthengine__apidocs__ee_imagecollection_first]
image = ee.ImageCollection('COPERNICUS/S2_SR').first()
m = geemap.Map()
m.center_object(image, 8)
vis = {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 5000}
m.add_layer(image, vis, 'first of S2_SR')
display(m)

# Image COPERNICUS/S2_SR/20170328T083601_20170328T084228_T35RNK (21 bands)
# type: Image
# id: COPERNICUS/S2_SR/20170328T083601_20170328T084228_T35RNK
# version: 1559715954270152
# 'bands': List (21 elements)
# properties: Object (82 properties)
display(image)
# [END earthengine__apidocs__ee_imagecollection_first]
