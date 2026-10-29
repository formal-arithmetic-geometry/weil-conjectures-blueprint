+++
id = "pur9-def-thom-class-affine"
kind = "definition"
title = "Thom class of affine space"
order = 3247
uses = ["pur9-def-orientation", "det-def-purity-conv"]
+++
Define $\mathrm{th}_c:(\mathcal O_E/\pi_E^n)_B\to Rz^!_{c,\mathcal O_E/\pi_E^n}\bigl((\mathcal O_E/\pi_E^n)_{\Aaf^c_B}(c)\bigr)[2c]$ recursively: $\mathrm{th}_0=\mathrm{id}$, $\mathrm{th}_1=\mathrm{pur}_{z_1}$ of Definition [pur9-def-orientation], and for $c\geq2$ $\mathrm{th}_c$ is the composite

$$
(\mathcal O_E/\pi_E^n)_B\xrightarrow{\mathrm{th}_{c-1}}Rz^!_{c-1,\mathcal O_E/\pi_E^n}\bigl((\mathcal O_E/\pi_E^n)_{B'}(c-1)\bigr)[2c-2]
\xrightarrow{Rz^!_{c-1,\mathcal O_E/\pi_E^n}(\mathrm{pur}_{s'}(c-1))}Rz^!_{c-1,\mathcal O_E/\pi_E^n}\bigl(Rs'^!_{\mathcal O_E/\pi_E^n}((\mathcal O_E/\pi_E^n)(1))(c-1)\bigr)[2c]
$$

$$
\xrightarrow{\ \tau^{-1}\ }Rz^!_{c-1,\mathcal O_E/\pi_E^n}Rs'^!_{\mathcal O_E/\pi_E^n}\bigl((\mathcal O_E/\pi_E^n)_{\Aaf^c_B}(c)\bigr)[2c]
\xrightarrow{\ c_{s',z_{c-1}}^{-1}\ }Rz^!_{c,\mathcal O_E/\pi_E^n}\bigl((\mathcal O_E/\pi_E^n)_{\Aaf^c_B}(c)\bigr)[2c],
$$

all exceptional functors at the coefficient $\mathcal O_E/\pi_E^n$, where $\tau$ is Lemma “The twist passage is canonical” (`pur9-lem-twist-passage`) for $\Phi=Rs'^!_{\mathcal O_E/\pi_E^n}$ (linear by Lemma “Linearity and shifts of the standing functors” (`pur9-lem-exceptional-linear`)) combined with Lemma “Additivity of twists” (`pur9-lem-twist-additivity`, in [det-def-purity-conv]), shifts are moved by Lemma “Linearity and shifts of the standing functors” (`pur9-lem-exceptional-linear`), and $c$ is Lemma “The exceptional composition comparison is invertible” (`pur9-lem-upper-shriek-composition`) for $z_c=s'z_{c-1}$.
