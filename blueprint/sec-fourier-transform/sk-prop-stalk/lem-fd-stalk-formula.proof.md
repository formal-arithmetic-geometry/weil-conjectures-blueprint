+++
kind  = "proof"
of    = "lem-fd-stalk-formula"
uses = ["sk-thm-sfb-shriek-base-change", "sk-prop-sf-cbc", "thm-fd-transform-well-defined", "def-fd-kernel", "def-fd-transform"]
+++
Form the cartesian square with $g=\bar\xi:\operatorname{Spec}\Omega\to V^\vee$ and $p_2:V\times_kV^\vee\to V^\vee$. Its base change $p_2':V_{\bar\xi}\to\operatorname{Spec}\Omega$ is the structure morphism of $V_{\bar\xi}\cong\mathbf A^r_\Omega$, and $g':V_{\bar\xi}\to V\times_kV^\vee$ is $(\mathrm{pr}_V,\bar\xi)$. The stalk at $\bar\xi$ of a complex on $V^\vee$ is its inverse image along $g$, so the compact-support base change on bounded constructible complexes ([sk-thm-sfb-shriek-base-change] for $\Lambda=E,\overline{\mathbf Q}_\ell$; see also [sk-prop-sf-cbc]), applied to this square and to $p_1^*K\otimes^L\mathcal K_\psi\in D^b_c(V\times_kV^\vee,\Lambda)$ ([thm-fd-transform-well-defined]), gives

$$
\bigl(Rp_{2!}(p_1^*K\otimes^L\mathcal K_\psi)\bigr)_{\bar\xi}
=Lg^*Rp_{2!}(p_1^*K\otimes^L\mathcal K_\psi)
\cong Rp'_{2!}\,Lg'^*(p_1^*K\otimes^L\mathcal K_\psi)
=R\Gamma_c\bigl(V_{\bar\xi},\,g'^*(p_1^*K\otimes^L\mathcal K_\psi)\bigr).
$$

Here $g'^*p_1^*K=K|_{V_{\bar\xi}}$, and $g'^*\mathcal K_\psi=g'^*b^*\mathcal L_\psi$ is the Artin–Schreier sheaf of the function $b\circ g'=\langle x,\xi\rangle$ on $V_{\bar\xi}$, because the base change of the twist is the twist by the base-changed function ([def-fd-kernel]): the inverse image of $\mathcal L_{\psi,f}$ along a morphism $h$ is $\mathcal L_{\psi,f\circ h}$, the Artin–Schreier covering being compatible with base change. With the shift $[r]$ of [def-fd-transform], this is the displayed formula. (The base change used is the proper, compact-support one along $\bar\xi\to V^\vee$, not smooth base change. If one passes instead through the strict henselization $\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{V^\vee,\bar\xi}$, the kernel on $V\times_k\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{V^\vee,\bar\xi}$ is $\mathcal L_{\psi(\langle x,\xi_{\mathrm{univ}}\rangle)}$ for the tautological point $\xi_{\mathrm{univ}}$, not the pullback of $\mathcal L_{\psi(\langle x,\xi\rangle)}$ from $V_{\bar\xi}$, and the passage to the closed fibre is again this compact-support base change.)
