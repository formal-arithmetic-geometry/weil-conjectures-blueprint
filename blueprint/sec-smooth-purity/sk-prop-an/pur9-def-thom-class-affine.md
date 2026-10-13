+++
id = "pur9-def-thom-class-affine"
kind = "definition"
title = "Thom class of affine space"
order = 2307
tags = ["latex:bpdefinition"]
uses = ["pur9-def-orientation", "pur9-lem-exceptional-linear", "pur9-lem-twist-additivity", "pur9-lem-twist-passage", "pur9-lem-upper-shriek-composition"]
+++
Define $\mathrm{th}_c:(\mathcal O_E/\varpi^n)_B\to Rz^!_{c,\mathcal O_E/\varpi^n}\bigl((\mathcal O_E/\varpi^n)_{\Aaf^c_B}(c)\bigr)[2c]$ recursively: $\mathrm{th}_0=\mathrm{id}$, $\mathrm{th}_1=\mathrm{pur}_{z_1}$ of Definition [pur9-def-orientation], and for $c\geq2$ $\mathrm{th}_c$ is the composite

$$
(\mathcal O_E/\varpi^n)_B\xrightarrow{\mathrm{th}_{c-1}}Rz^!_{c-1,\mathcal O_E/\varpi^n}\bigl((\mathcal O_E/\varpi^n)_{B'}(c-1)\bigr)[2c-2]
\xrightarrow{Rz^!_{c-1,\mathcal O_E/\varpi^n}(\mathrm{pur}_{s'}(c-1))}Rz^!_{c-1,\mathcal O_E/\varpi^n}\bigl(Rs'^!_{\mathcal O_E/\varpi^n}((\mathcal O_E/\varpi^n)(1))(c-1)\bigr)[2c]
$$

$$
\xrightarrow{\ \tau^{-1}\ }Rz^!_{c-1,\mathcal O_E/\varpi^n}Rs'^!_{\mathcal O_E/\varpi^n}\bigl((\mathcal O_E/\varpi^n)_{\Aaf^c_B}(c)\bigr)[2c]
\xrightarrow{\ c_{s',z_{c-1}}^{-1}\ }Rz^!_{c,\mathcal O_E/\varpi^n}\bigl((\mathcal O_E/\varpi^n)_{\Aaf^c_B}(c)\bigr)[2c],
$$

all exceptional functors at the coefficient $\mathcal O_E/\varpi^n$, where $\tau$ is Lemma [pur9-lem-twist-passage] for $\Phi=Rs'^!_{\mathcal O_E/\varpi^n}$ (linear by Lemma [pur9-lem-exceptional-linear]) combined with Lemma [pur9-lem-twist-additivity], shifts are moved by Lemma [pur9-lem-exceptional-linear], and $c$ is Lemma [pur9-lem-upper-shriek-composition] for $z_c=s'z_{c-1}$.
