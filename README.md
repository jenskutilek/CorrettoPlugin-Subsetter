# Corretto Subsetter

A subsetter plugin for Corretto. Apply subsetting to fonts, generate language variants and trial fonts, limit variation axes in font files after export.

## How It Works

The Corretto Subsetter is a Glyphs plugin for the
[Corretto Post-Processor](https://github.com/jenskutilek/CorrettoPlugin).

When you have the Corretto plugin installed, it will get called whenever you
export a font. It will then check for any custom parameters using a special
prefix (`de.kutilek.corretto...`), which are used to configure Corretto’s
operation.

The Corretto Subsetter is configured via the Custom Parameter `de.kutilek.corretto.subset` in an export setting in your Glyphs file, either in a Variable Font Setting, or a static Export.

## This is an evaluation version!

The Corretto Subsetter is a commercial plugin. It will run as an evaluation version with
full functionality for 10 days.

## Installation

Make sure you have the main Corretto Post-Processing Plugin installed via the Glyphs
Plugin Manager.
[See the installation guide](https://corretto.kutilek.de/manual/installation) for
details. Then download the Corretto Subsetter [from the latest release page](https://github.com/jenskutilek/CorrettoPlugin-Subsetter/releases) and drag it onto the
Glyphs app icon in Finder or in your Dock. Restart Glyphs.

To **enable automatic updates** for the Corretto Subsetter, don’t download the release;
clone the repo and drag the `CorrettoSubsetter.glyphsPlugin` from there onto the Glyphs
app icon. When prompted, choose to make an alias.

To run the Subsetter, Corretto must know about it. Add an entry to your [global.correttoconfig.yaml](global.correttoconfig.yaml) as shown.

Try to export the variable fonts from the demo folder to see if the Subsetter is
working.

## Configuration Options

### de.kutilek.corretto.subset

Save a copy of the font with subsetted character set, and, for variable fonts,
limited axis ranges. The family name can be replaced or suffixed in the process.
The subsetting is controlled via an external YAML file, the path to which is
read from the custom parameter. The path is relative to the Glyphs file.

**Why?** Produce alternate versions of your fonts with ease.

-   Generate trial fonts always in sync with your full fonts.
-   From a master file with weight and width axes, export a separate variable font for each width with a weight axis.
-   Generate smaller webfonts which only contain one writing system, with other writing
    systems as fallback fonts.

Format:

```
relative_file_path
```

Example:

```
{
  customParameters = (
    {
      name = de.kutilek.corretto.subset;
      value = MyFont.correttosubsetter.yaml;
    }
  );
}
```

This means: Save additional versions of the exported font(s) as specified in the
configuration file `MyFont.correttosubsetter.yaml`, which is located next to the Glyphs
file itself.

A YAML schema file `CorrettoSubsetter.schema.yaml`, is included inside the plugin’s
Resources folder. Configure your text editor, e.g. VSCode, to use it for files matching
`*.correttosubsetter.yaml` to get live syntax checking and autocompletion.

## Copyright

© 2024–2025 by Jens Kutilek. All rights reserved.
