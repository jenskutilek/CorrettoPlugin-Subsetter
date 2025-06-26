# Corretto Subsetter

A subsetter plugin for the [Corretto Post-Processor](https://github.com/jenskutilek/CorrettoPlugin) which in turn is a plugin for the font editor [Glyphs](https://glyphsapp.com).

**Why?** Produce alternate versions of your fonts with ease. Just some ideas:

-   **Generate trial fonts** always in sync with your full fonts, with a reduced character set and “Trial” added to the family name
-   From a master file with weight and width axes, export a **separate variable font for each width with a weight axis.**
-   Generate smaller webfonts which only contain **one writing system,** with other writing
    systems as fallback fonts.
-   Split your font into **separate language versions** e.g. for Latin, Greek, Cyrillic, Arabic ...
-   **Limit variation axes** so your customers can license a part of the full range

## How It Works

The Corretto Subsetter is a Glyphs plugin for the
[Corretto Post-Processor](https://github.com/jenskutilek/CorrettoPlugin).

When you have the Corretto plugin installed, it will get called whenever you
export a font.

The Corretto Subsetter is configured via the Custom Parameter
`de.kutilek.corretto.subset` in an export setting in your Glyphs file, either in a
**Variable Font Setting,** or a static **Export.**

## This is an evaluation version!

The Corretto Subsetter is a commercial plugin. It will run as an evaluation version with
full functionality for 10 days.

## Installation

Make sure you have the main Corretto Post-Processing Plugin installed via the **Plugin
Manager** inside Glyphs.
[See the installation guide](https://corretto.kutilek.de/manual/installation) for
details.

There are two options to install the Corretto Subsetter:

1. Recommended: To **enable automatic updates** for the Corretto Subsetter, clone this
   git repository and drag the `CorrettoSubsetter.glyphsPlugin` from there onto the
   Glyphs app icon. When prompted, choose to make an alias.
2. Without automatic updates: Download the Corretto Subsetter [from the latest release
   page](https://github.com/jenskutilek/CorrettoPlugin-Subsetter/releases), unzip it, and drag it onto the Glyphs app icon in Finder or in your Dock.

Restart Glyphs.

To run the Subsetter, Corretto must know about it. Add an entry to the end of the configuration file [~/Library/Application Support/Glyphs 3/global.correttoconfig.yaml](global.correttoconfig.yaml) as shown:

```yaml
corretto:
    plugins:
        - module: corretto.plugins.MathTable
        - module: corretto.plugins.MergeTTX
        - module: corretto.plugins.FixedPitch
        - module: corretto.plugins.GaspTable
        - module: corretto.plugins.DeltaBase
        - module: corretto.plugins.MaxpStack
        - module: corretto.plugins.HeadTable
        - module: corretto.plugins.VariableFontMetrics
        - module: corretto.plugins.Save
        - module: corretto.plugins.SaveTTX
        - module: corretto.plugins.Webfonts
        - module: CorrettoSubsetter # Add this line to your configuration!
```

## Examples

Try to export the variable fonts from the `demo` folder to see if the Subsetter is
working.

Also see the commented examples on the Corretto website:

-   [Trial Fonts](https://corretto.kutilek.de/examples/trial-fonts)
-   [Make a Windows-1252 Variable Font Subset With Only R/I/B/BI Styles](https://corretto.kutilek.de/examples/win-1252)
-   [Split a Variable Font Into Separate Roman and Italic Fonts](https://corretto.kutilek.de/examples/split-italic-vf)

## Configuration via Custom Parameter

### de.kutilek.corretto.subset

The subsetting is controlled via an external configuration file in YAML format, the path
to which is read from the custom parameter. The path is relative to the Glyphs file.

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

You can copy and paste the above code to the **Font Info** in Glyphs.

This means: Save additional versions of the exported font(s) as specified in the
configuration file `MyFont.correttosubsetter.yaml`, which is located next to the Glyphs
file itself.

A YAML schema file, `CorrettoSubsetter.schema.yaml`, is included inside the plugin’s
`Resources` folder. Configure your text editor, e.g. VSCode, to use it for files matching
`*.correttosubsetter.yaml` to get live syntax checking and autocompletion.

## Copyright

© 2024–2025 by Jens Kutilek. All rights reserved.
