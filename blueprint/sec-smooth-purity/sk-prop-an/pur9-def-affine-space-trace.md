+++
id = "pur9-def-affine-space-trace"
kind = "definition"
title = "Trace of affine space"
order = 2320
tags = ["latex:bpdefinition"]
uses = ["pur9-def-affine-line-trace", "pur9-input-ambient-composition", "pur9-lem-twist-additivity", "pur9-lem-twist-passage"]
+++
Under the inputs of Definition [pur9-def-affine-line-trace], define $\int_{p_c}:Rp_{c,!,\mathcal O_E/\varpi^n}((\mathcal O_E/\varpi^n)_{\Aaf^c_B}(c))[2c]\to(\mathcal O_E/\varpi^n)_B$ recursively: $\int_{p_0}=\mathrm{id}$, $\int_{p_1}=\int_p$ of Definition [pur9-def-affine-line-trace] over $B$, and for $c\geq2$ the composite of $\alpha_{p_{c-1},p'}^{-1}$ (Input [pur9-input-ambient-composition]), the twist passage $\tau$ of Lemma [pur9-lem-twist-passage] for $\Phi=Rp'_{!,\mathcal O_E/\varpi^n}$ with Lemma [pur9-lem-twist-additivity], $Rp_{c-1,!,\mathcal O_E/\varpi^n}(\int_{p'}(c-1))$ with $\int_{p'}$ over $B'$, and $\int_{p_{c-1}}$.
