+++
kind  = "proof"
of    = "sk-prop-stalk"
+++
Form the Cartesian square with $g=\bar\xi:\Spec\Omega\to V^\vee$ and
$p_2:V\times_kV^\vee\to V^\vee$; its base change
$p_2':V_{\bar\xi}\to\Spec\Omega$ is the structure morphism of
$V_{\bar\xi}\cong\mathbf A^{r}_\Omega$, and $g':V_{\bar\xi}\to V\times_kV^\vee$
is $(\mathrm{pr}_V,\bar\xi)$. The stalk at $\bar\xi$ of a complex on
$V^\vee$ is its inverse image along $g$, so compact-support base change on bounded constructible complexes
([sk-thm-sfb-shriek-base-change], [sk-prop-sf-cbc], with coefficients
$\Lambda=E$ or $\Qlb$ on $\Dbc$, where $p_1^*K$ and the kernel live) gives

$$
\bigl(Rp_{2!}(p_1^*K\otimes^L\mathcal K_\psi)\bigr)_{\bar\xi}
=Lg^*Rp_{2!}(p_1^*K\otimes^L\mathcal K_\psi)
\cong Rp'_{2!}\,Lg'^*(p_1^*K\otimes^L\mathcal K_\psi)
=R\Gamma_c\bigl(V_{\bar\xi},\,g'^*(p_1^*K\otimes^L\mathcal K_\psi)\bigr).
$$

Here $g'^*p_1^*K=K|_{V_{\bar\xi}}$, and
$g'^*\mathcal K_\psi=g'^*b^*\mathcal L_\psi$ is the Artin–Schreier sheaf of
the function $b\circ g'=\langle x,\xi\rangle$ on $V_{\bar\xi}$, because the
inverse image of $\mathcal L_{\psi,f}$ along a morphism $h$ is
$\mathcal L_{\psi,f\circ h}$ (the Artin–Schreier covering of [sk-def-as]
is compatible with base change). Taking cohomology and inserting the shift
$[r]$ of [sk-def-ft] gives the formula. The base change used is the
proper, i.e. compact-support, one along $\bar\xi\to V^\vee$; smooth base
change is not what is needed here. (If one instead passes through the
strict henselization $\Spec\mathcal O^{\mathrm{sh}}_{V^\vee,\bar\xi}$, the
kernel on $V\times_k\Spec\mathcal O^{\mathrm{sh}}_{V^\vee,\bar\xi}$ is
$\mathcal L_{\psi(\langle x,\xi_{\mathrm{univ}}\rangle)}$ for the tautological
point $\xi_{\mathrm{univ}}$, not the pullback of
$\mathcal L_{\psi(\langle x,\xi\rangle)}$ from $V_{\bar\xi}$, and the passage
to the closed fibre is again this compact-support base change.)
