+++
kind  = "proof"
of    = "lem-zl-affine-curve-range"
uses = ["def-compact-support-direct-image-detailed", "sk-lem-coefficient-heart", "sk-thm-sfb-qlbar-two-colimit", "sk-prop-sfb-finite-extension-compatibility", "sk-lem-stratified-lattice", "sk-prop-scalar-six", "sk-prop-integral-criterion", "sk-thm-sf-ctf-stability", "sk-def-pe-derived-completion", "lem-sc-cohomological-dimension", "lem-sc-compactification", "lem-weil-pbc-mittag-leffler", "sbc-thm-finiteness-finite-type"]
+++
The Weil structure plays no role; we bound the cohomology of the underlying
$\Qlb$-sheaf. Choose a smooth proper completion $j:C\hookrightarrow\overline C$
by [lem-sc-compactification].

*Torsion coefficients.* For a constructible sheaf $\mathcal G$ of
$\mathcal O_E/\pi_E^n$-modules on an open $U\subseteq C$, with
$j_U:U\hookrightarrow\overline C$,

$$
R\Gamma_c(U,\mathcal G)=R\Gamma(\overline C,j_{U!}\mathcal G)
$$

by [def-compact-support-direct-image-detailed]. The object $j_{U!}\mathcal G$ is
a sheaf in degree zero, so the cohomological-dimension bound
[lem-sc-cohomological-dimension](a) gives vanishing outside degrees $0,1,2$,
and the groups $H^r(\overline C,j_{U!}\mathcal G)$ are finite by
[sbc-thm-finiteness-finite-type] applied to the proper structure morphism of
$\overline C$.

*Reduction to $E$-coefficients.* By [sk-thm-sfb-qlbar-two-colimit](3) there are
a finite $E/\Ql$ and $K\in\Dbc(C,E)$ with $K_{\Qlb}\simeq\mathcal F$. Extension of
scalars along $E_C\to\overline{\mathbf Q}_{\ell,C}$ is exact
([sk-prop-sfb-finite-extension-compatibility]), so $\mathcal F_E:=H^0(K)$ is a
constructible $E_C$-module with $(\mathcal F_E)_{\Qlb}\simeq\mathcal F$. Since
$R\Gamma_c$ commutes with extension of scalars ([sk-prop-scalar-six]) and
$\Qlb$ is flat over $E$,
$H^i_c(C,\mathcal F)\simeq H^i_c(C,\mathcal F_E)\otimes_E\Qlb$. It suffices to
treat $\mathcal F_E$.

*Dévissage.* By [sk-lem-coefficient-heart](3) and the lattice lemma
[sk-lem-stratified-lattice], there are a dense open $u:U\hookrightarrow C$ and an
exact sequence $0\to u_!L\to\mathcal F_E\to i_*G\to0$, with $L$ a lisse
$E_U$-module containing a lisse $\mathcal O_{E,U}$-submodule $L_0$ with
$L_0[1/\ell]=L$, and $i_*G$ supported on finitely many closed points (shrink $U$
to a stratum on which the lattice exists). Compactly supported cohomology of a
sheaf on finitely many points is concentrated in degree $0$. By the long exact
sequence it therefore suffices to show $H^i_c(U,L)=0$ for $i\notin\{0,1,2\}$.

*Lattice.* Localization $\mathcal O_E\to E$ is one of the coefficient maps of
[sk-prop-scalar-six], so $H^i_c(U,L)\simeq H^i_c(U,L_0)\otimes_{\mathcal O_E}E$.
Put $M=R\Gamma_c(U,L_0)\in\Dbc(\operatorname{Spec}k,\mathcal O_E)$
([sk-thm-sf-ctf-stability]). It is derived $\pi_E$-complete
([sk-prop-integral-criterion]), so
$M\simeq R\varprojlim_nM\otimes^{\mathbf L}\mathcal O_E/\pi_E^n$
([sk-def-pe-derived-completion]); and since $L_0$ is flat and reduction modulo
$\pi_E^n$ commutes with $R\Gamma_c$ ([sk-prop-scalar-six]),
$M\otimes^{\mathbf L}\mathcal O_E/\pi_E^n\simeq R\Gamma_c(U,L_0/\pi_E^n)$. These
are torsion complexes with finite cohomology concentrated in degrees $0,1,2$, by
the torsion case. By [lem-weil-pbc-mittag-leffler],
$H^i(M)\simeq\varprojlim_nH^i_c(U,L_0/\pi_E^n)$, which vanishes for
$i\notin\{0,1,2\}$. Inverting $\ell$ gives the assertion for $L$, hence for
$\mathcal F_E$ and $\mathcal F$.

The argument concerns sheaves in degree zero: an arbitrary shift of such a
sheaf would shift the cohomological range.
