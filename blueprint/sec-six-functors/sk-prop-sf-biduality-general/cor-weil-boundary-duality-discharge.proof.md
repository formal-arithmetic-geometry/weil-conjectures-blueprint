+++
kind  = "proof"
of    = "cor-weil-boundary-duality-discharge"
+++
Preservation in the first clause of
[def-weil-boundary-duality-input] is part of
[thm-fix-general-biduality], applied to every piece.
The independently formal comparison
$\alpha_{D_TL}:Ri^!D_TD_TL\cong D_Zi^*D_TL$ of
[lem-weil-closed-costalk-duality], composed with $Ri^!\delta_L$,
identifies $Ri^!L$ with $D_Zi^*D_TL$.
In particular $Ri^!L$ is finite-Tor constructible. Apply $D_Z$
and use biduality on $Z$:

$$
D_ZRi^!L\cong D_ZD_Zi^*D_TL\cong i^*D_TL.
$$

The inverse of this composite is $\beta_L$. Indeed, adjointing
back through tensor–Hom and $i_*\dashv Ri^!$, both maps correspond
to the restriction of the evaluation
$D_TL\otimes^L L\to\omega_T$. The evaluation identities in
[lem-weil-duality-pairing] then also give exactly the compatibility
between $\beta_{D_TK}$, $\alpha_K$, and $i^*\delta_K$ required
in the second clause of the definition. Thus boundary exchange is
derived after biduality and was not used to prove it.
