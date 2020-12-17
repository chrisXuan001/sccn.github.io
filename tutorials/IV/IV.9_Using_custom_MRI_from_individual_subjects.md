---
layout: default
title: IV.9 Using custom MRI from individual subjects
parent: IV. Appendix
grand_parent: Tutorials
nav_order: 9
---

{ {Backward_Forward\|A08:_DIPFIT\|A08: The DIPFIT Plug-In\|A10:
MI-clust\|A10: The MI-clust Plug-In} }

To visualize dipoles (DIPFIT plugin) or distributed source activity
(LORETA plugin) within subject's individual MRI, it is first necessary
to normalize them to the MNI brain template. The procedure is relatively
simple and is explained below.

Normalizing an MR head image to the MNI brain template
------------------------------------------------------

Normalizing an anatomical MR brain image to the standard MNI brain is
quite simple and does not require specialized knowledge about MRI or
fMRI data. First, download
[SPM2](http://sourceforge.net/project/showfiles.php?group_id=45102&package_id=73148),
uncompress, add path in Matlab. Start spm by typing *\>\> spm* on the
Matlab command line.



![425px](/assets/images/Spm_entryscreen.gif)



Next, click on the *fMRI time series* button. The following menu will
appear (along with other screens).



![425px](/assets/images/Spm_menu.gif)



Click on the display button and select your anatomical MR image file by
clicking on it. Then press, *Done* as shown below.



![325px](/assets/images/Spm_selectdisplay.gif)


A display screen as shown below will appear. Your MR image must be
oriented as the one shown below. If it is otherwise oriented, use the
edit boxes: *Pitch*, *Roll* and *Yaw* to rotate it in 3-D until it
matches the template below. Then press the *Reorient image* button on
the bottom.



![525px](/assets/images/Spm_displayscreen.gif)



The next step is to normalize your MRI to the standard MNI brain image.
To do this, press the *Normalize* button in the main menu below. A blue
tab will appear below the main menu. Select *Determine Parameters &
Write Normalized*.



![375px](/assets/images/Spm_normalize.gif)


The following file selection window will appear. Select *T1.mnc*, the
most common MRI format. (See the SPM manual for other formats). Then
press *Done*.




![375px](/assets/images/Spm_selecttemplate.gif)



Then reselect MRI data file (the same one you selected originally).
Press *Done*.



![425px](/assets/images/Spm_selectsource.gif)


Another file selection window will appear asking for the name of the
file to write. Reselect once more the same MRI data file as the output
file. SPM2 will not overwrite it but will use its name. Press *Done*. A
final window will appear asking for data for a second subject. Simply
press *Done* again. SPM2 will take a few minutes to normalize your MRI
to the MNI brain. (It first segments your image and then compares the
segmentation to the segmented MNI brain). The output file will have the
same name as your original file, but with the prefix "w". You may use
this file in the DIPFIT interface as the background image. An example is
shown below:



![425px](/assets/images/Dipplot_spm.gif)


Note that the resolution of this MR image is relatively low and appears
noisy because of the renormalization process used in SPM2. If you use
other software to perform the normalization, EEGLAB should be able to
read the output image using the Fieldtrip function *read_fcdc_mri()* to
import various MRI data formats.


*Thanks to J-R Duann for helpful advice - Arnaud Delorme, March 2005*.
[Category:IV. Appendix](/Category:IV._Appendix "wikilink") {
{Backward_Forward\|A08:_DIPFIT\|A08: The DIPFIT Plug-In\|A10:
MI-clust\|A10: The MI-clust Plug-In} }