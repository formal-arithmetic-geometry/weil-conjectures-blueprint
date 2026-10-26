+++
id = "pur9-def-affine-space-trace"
kind = "definition"
title = "Trace of affine space"
order = 2893
uses = ["pur9-def-affine-line-trace", "sk-def-purity-conv"]
+++
Under the inputs of Definition [pur9-def-affine-line-trace], define $\int_{p_c}:Rp_{c,!,\mathcal O_E/\pi_E^n}((\mathcal O_E/\pi_E^n)_{\Aaf^c_B}(c))[2c]\to(\mathcal O_E/\pi_E^n)_B$ recursively: $\int_{p_0}=\mathrm{id}$, $\int_{p_1}=\int_p$ of Definition [pur9-def-affine-line-trace] over $B$, and for $c\geq2$ the composite of $\alpha_{p_{c-1},p'}^{-1}$ (Input “Composition of standing compact-support direct images” (`pur9-input-ambient-composition`)), the twist passage $\tau$ of Lemma “The twist passage is canonical” (`pur9-lem-twist-passage`) for $\Phi=Rp'_{!,\mathcal O_E/\pi_E^n}$ with Lemma “Additivity of twists” (`pur9-lem-twist-additivity`, in [sk-def-purity-conv]), $Rp_{c-1,!,\mathcal O_E/\pi_E^n}(\int_{p'}(c-1))$ with $\int_{p'}$ over $B'$, and $\int_{p_{c-1}}$.
