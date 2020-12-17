---
layout: default
title: c. Channel Locations
parent: 4. Import data
grand_parent: Tutorials
---
Importing channel locations
===========================

To plot EEG scalp maps in either 2-D or 3-D format, or to estimate
source locations of data components, an EEGLAB dataset must contain
information about the scalp locations of the recording electrodes.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>


Load the sample EEGLAB dataset
------

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>.

![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/Pop_loadset.png)

Select the tutorial file "eeglab_data.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

Look up channel location
------

This section does not use the tutorial dataset. It intent is to provide
guidelines for automatically finding channel locations when channel
names are known. For instance, when importing a Neuroscan, or a
Biosemi channel locations file, channel names are often stored in the
file header. EEGLAB will automatically read these channel labels. When
you then call the channel editing window, the function will look up
10-10 channel locations in a database of 385 defined channel labels, the file
"Standard-10-5-Cap385.sfp" in the "function/resources" sub-folder of the
EEGLAB distribution. You may add additional standard channel locations
to this file if you wish. As of 2021, the default
channel location file for electrode position is the MNI file, which is best suited for source localization. Prior to 2021,
it was the BESA spherical location file.

To load or edit channel location information contained in a dataset,
select <span style="color: brown">Edit → Channel locations</span>.
A dialog box (shown below) will appear, asking you if you want
to use standard channel locations based on the imported electrode
position labels (for example 'Fz') from a channel locations file using
an extended International 10-20 System.

![Image:Editchannelinfo_auto.png]({{ site.baseurl }}/assets/images/Editchannelinfo_auto.png)

You may choose between several templates. If you intend to perform
source localization, we strongly suggest that you select the second
option "Use MNI coordinates for the BEM Dipfit model" (the first set
of 'BESA' coordinates was designed for a spherical BESA head model,
now obsolete). Press *OK*.

![500px]({{ site.baseurl }}/assets/images/Gui_pop_chanedit2.jpg)

### Command line channel location look up example

Below, we will build a channel structure using channel labels only,
then will call the channel editing window. In the Matlab command window,
type:

```matlab
chanlocs = struct('labels', { 'cz' 'c3' 'c4' 'pz' 'p3' 'p4' 'fz' 'f3' 'f4'});
pop_chanedit( chanlocs );
```

Then call <span style="color: brown">Edit → Channel locations</span> and look up channel locations. Press *Plot 2-D* to plot the channel locations. Close the channel editing window (using *Cancel* to discard the entered locations), then proceed to the next section.

![Image:Topoplotlookup.gif](/assets/images/Topoplotlookup.gif)

Load channel location from file
------

Reopen <span style="color: brown">Edit → Channel locations</span>. In case it is not possible to look up channel locations based on their labels, or in case you have a scanned electrode file available, to load a channel locations file, press the *Read Locations* button. For the current data file, you may  select the sample channel locations file *eeglab_chan32.locs*
(located in the *sample_data* sub-directory of the EEGLAB
distribution).

![Image:Loadchannellocation.png]({{ site.baseurl }}/assets/images/Loadchannellocation.png)

If you do not specify
the file format, the [pop_chanedit.m]() function will attempt
to use the filename extension to assess its format. Press the button
*Read locs help* in the main channel graphic interface window to view
the supported formats. In the next pop-up window, simply press *OK*. 

![250px]({{ site.baseurl }}/assets/images/Chanedit_fileformat_gui.jpg)

In the window below, you may scroll through the channel field values
1-by-1 using the *\<* and *→* buttons, or in steps of 10 using *\<\<*
and *\>\>*.

![500px]({{ site.baseurl }}/assets/images/Gui_pop_chanedit2.jpg)

The *Set channel type* button allows you to enter a *channel type*
associated with the channel (for example, 'EEG', 'MEG', 'EMG', 'ECG',
'Events', etc.). Channel types may be used
by other EEGLAB functions to restrict plotting and computation to a desired subset of channel types,
allowing easier analysis of multi-modal datasets. It is therefore well
worth the effort to add channel types to your data. It is important to
press *OK* in the channel editing window above to actually import the
channel locations!. Note that in the main EEGLAB window, the *channel location* flag now shows *yes*.

Viewing Channel Locations
------

Reopen <span style="color: brown">Edit → Channel locations</span> if you closed it. 

### Plot channel location in 2-D

To visualize the 2-D locations of the channels, press *Plot
2-D* above the *Read Locations* button. Else, at any time during an EEGLAB session you may refer to a plot showing the channel locations
by selecting <font color=brown>Plot → Channel location → By
name</font>. 
Either command pops up a window like that below. We recommend using the default settings.

*Note*: In
this plot, click on any channel label to see its channel number.

![Image:Channellocationname.png]({{ site.baseurl }}/assets/images/Channellocationname.png)

<span style="color: red">WARNING</span>: Equating 'channel locations' with
(single) *electrode* locations only makes sense when all channels use
the same 'reference channel.' An EEG channel signal is always the
difference between voltages at two (or more) electrodes --
typically some electrode "referred to" a reference channel (or channel
combination). Equating the signal 'channel location' to the location of
one of the contributing electrodes is quite imprecise, as the channel
must be equally sensitive to potentials flowing to *either* of its two
(or more) contributing scalp electrodes.
 
Electrodes plotted outside the head cartoon are electrodes located below the mid-head line (i.e.,
with a negative z (height) coordinate, 0 being the center of the
head). They are plotted outside the head cartoon by convention. To plot scalp maps only inside the head cartoon, enter 0.5 in the *Plot
radius* edit box. In this case, the two eye electrodes will not be
displayed nor taken into account when computing interpolated 2-D scalp
maps for display or (in some cases) further processing. These settings are used for all scalp topographies plotted in EEGLAB. 

If you do not see enough of the recorded field, set this dialogue box to 1.0 to
interpolate and show scalp maps including all possible scalp channel
locations, with parts of the head below the (0.5) head equator shown
in a 'skirt' or 'halo' region outside the cartoon head boundary (more
precise separate controls of which channel locations to plot are
available from the command line: see the 'Help' message for the scalp
map plotting function [topoplot.m]()).

### Why are electrodes plotted outside of the head limits?
  
In the previous image, electrode EOG1 and EOG2 are plotted beyong the head limit because they extends below the
horizontal plane of the head center. [topoplot](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m) plots them
outside the cartoon head that marks the
(arc_length = 0.5) head-center plane. By
default, all channels with location arc_lengths \<= 1.0 (head bottom)
are used for interpolation and are shown in the plot. From the
commandline, [topoplot](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m) allows the user to specify the
interpolation and plotting radii (*intrad* and *plotrad*) as well as the
radius of the cartoon head (*headrad*). The *headrad* value should
normally be kept at its physiologically correct value (0.5) and for this reason, it is not possible to change it in the EEGLAB graphical interface.

When plotting in 2-D, the distance of the electrode positions from the vertex, however,
is proportional to their (great circle) distance on the scalp to the
vertex. This keeps the electrodes on the sides of the head from being
bunched together as they would be in a top-down view of their positions.
This great-circle projection spreads out the positions of the lower
electrodes. Thus, in the figure above, the (top) electrodes plotted
on the lower portion of the 'skirt' are actually located on the lower part of the face. In the plot, they may appear spread out, whereas in reality they
are bunched on the relatively narrow face surface. The combinations of
top-down and great-circle projections allows the full component
projection (or raw data scalp map) to be seen clearly, while allowing
the viewer to estimate the actual 3-D locations of plot features.
Importing continuous and epoched data

### Plot channel location in 3-D

To visualize the channel locations in 3-D, press *Plot 3-D (xyz)*. The
window below will appear. The plotting box can be rotated in 3-D using
the mouse:

![Image:3dlpotxyz.gif](/assets/images/3dlpotxyz.gif)

Now the loaded channel labels and coordinates are displayed in
the [pop_chanedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanedit.m) window. Note that the channel editor keeps polar to carthesian to spherical coordinate consistent. If you load a file containing polar coordinates for channel labels, they are automatically converted to carthesian and sperical coordinate. You may change channel locations manually using the edit box provided
for each channel's coordinates. However, after each change, you must
update the other coordinate formats. For instance, if you update the
polar coordinates for one channel, then press the *polar → sph. & xyz*
button on the right of the [pop_chanedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanedit.m) window (see
above) to convert these values to other coordinate formats.

Supported Data Formats
-------------------------------------

Supported data format are described in the help message of the [readlocs.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=readlocs.m) function. Supported formats include:

- '.loc', '.locs', '.eloc' file extensions: EEGLAB polar coordinate files
- '.ced' extension: EEGLAB files containing polar, carthesian and spherical coordinates
- '.sph' extension: Matlab spherical coordinates
- '.elc' extension: Cartesian 3-D electrode coordinates scanned using the EETrak software. 
- '.elp' extension: Polhemus-.'elp' Cartesian coordinates
- '.elp' extension: BESA-'.elp' spherical coordinates
- '.xyz' extension: Matlab/EEGLAB Cartesian coordinates
- '.asc' and '.dat' extensions: Neuroscan-.'asc' or '.dat' Cartesian polar coordinates text file.
- '.mat' extension: Brainstrom channel location file.
- '.sfp' extension: BESA/EGI-xyz Cartesian coordinates

This [readlocs.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=readlocs.m) function (which is called by channel editor) can also import custom channel location files where coordinate information is contained in different columns. Following are examples of ascii channel locations data in EEGLAB-supported formats. Note that in all the examples below, the first header line must not be present.

-   Four channels from a polar coordinates file (with filename extension
    *.loc*, Do not include the (light blue) header line:

<table>
<tbody>
<tr>
<td><b>#</b>
</td>
<td><b>Deg.</b>
</td>
<td><b>Radius</b>
</td>
<td><b>Label</b>
</td>
</tr>
<tr>
<td>1
</td>
<td>-18
</td>
<td>,352
</td>
<td>Fp1
</td>
</tr>
<tr>
<td>2
</td>
<td>18
</td>
<td>.352
</td>
<td>Fp2
</td>
</tr>
<tr>
<td>3
</td>
<td>-90
</td>
<td>,181
</td>
<td>C3
</td>
</tr>
<tr>
<td>4
</td>
<td>90
</td>
<td>,181
</td>
<td>C4</td>
</tr>
</tbody>
</table>


- The same locations, from a spherical coordinates file (estension, *.sph* ):

<table>
<tbody>
<tr>
<td><b>#</b></td>
<td><b>Azimut</b></td>
<td><b>Horiz.</b></td>
<td><b>Label</b></td>
</tr>
<tr>
<td>1</td>
<td>-63.36</td>
<td>-72</td>
<td>Fp1</td>
</tr>
<tr>
<td>2</td>
<td>63.36</td>
<td>72</td>
<td>Fp2</td>
</tr>
<tr>
<td>3</td>
<td>32.58</td>
<td>0</td>
<td>C3</td>
</tr>
<tr>
<td>4</td>
<td>32.58</td>
<td>0</td>
<td>C4</td>
</tr>
</tbody>
</table>


- The same locations from a Cartesian coordinates file (extension, *.xyz* ):

<table>
<tbody>
<tr>
<td><b>#</b>
</td>
<td><b>X</b>
</td>
<td><b>Y</b>
</td>
<td><b>Z</b>
</td>
<td><b>Label</b>
</td>
</tr>
<tr>
<td>1</td>
<td>-0.8355</td>
<td>-0.2192</td>
<td>-0.5039</td>
<td>Fp1</td>
</tr>
<tr>
<td>2</td>
<td>-0.8355</td>
<td>0.2192</td>
<td>0.5039</td>
<td>Fp2</td>
</tr>
<tr>
<td>3</td>
<td>0.3956</td>
<td>0</td>
<td>-0.9184</td>
<td>C3</td>
</tr>
<tr>
<td>4</td>
<td>0.3956</td>
<td>0</td>
<td>0.9184</td>
<td>C4</td>
</tr>
</tbody>
</table>

Note using the *Save (other type)* button of the channel editing window also allow converting between channel location file formats.

Adjusting scanned 3-D channel locations
------------------------------

This section does not use the tutorial dataset. Its intent is to provide
guidelines for importing channel locations measured in Cartesian
coordinates using 3-D tracking devices (such as Polhemus). Use the
EEGLAB menu <font color=brown>Edit → Channel location</font> or type
the following command on the Matlab command line:

```matlab
pop_chanedit([]);
```

An empty channel editing window will appear:

![Image:Editchannelinfo.jpg](/assets/images/Editchannelinfo.jpg)

Press the *Read locations* button and select the file *scanned72.dat*
from the *sample_data* subfolder of the EEGLAB distribution. This is a
channel locations file measured with the Polhemus system using Neuroscan
software (kindly supplied by Zoltan Mari). Use *autodetect* for
the file format. When the file has been imported, set plotting radius to 0.6 to mask some references points when plotting. Then, press the *Plot 2-D*
button. The following plot will pop up.

![Image:Scanlocs1.gif](/assets/images/Scanlocs1.gif)

As you can see, the measured 3-D channel coordinates may not be
accurately distributed on the 2-D head model. This is because the
measured values have not been shifted to the head center. To fix this
problem, you must first find the head sphere center that best fits the
imported 3-D electrode locations. To do so, press the *Opt. head center*
(optimize head center). The following window will pop up:

![Image:Pop_chancenter.gif](/assets/images/Pop_chancenter.gif)

Possibly, some of the channels should not be included in the head center
optimization, if they are not on the head and/or do not have recorded
locations. Enter electrodes indices to use (here, 1:3 33 35 64:72) in
the edit window. You may also press the *Browse* button above to select
channels that are not on the head. When you press *OK* in the browser
window, the channel indices will be copied, as shown in the window
above. Then press *Ok*. After the optimization has finished, press the
*Plot 2-D* button once more.

![Image:Scanlocs2.gif](/assets/images/Scanlocs2.gif)

In the view above, some channel locations are still incorrect. For
instance, you may expect channel "Cz" to be at the vertex (plot center).
To adjust this, press the *Rotate axis* button. The following window
will pop up:

![Image:Forcelocs.gif](/assets/images/Forcelocs.gif)

Simply press *OK* to align channel 'Cz' to the vertex (by default). Then
press the *Plot 2-D* button once more to again plot the scalp map.

![Image:Scanlocs3.gif](/assets/images/Scanlocs3.gif)

This section has illustrated operations you may want to perform to adapt
measured 3-D channel locations for use in EEGLAB. You may now close the channel editing window.