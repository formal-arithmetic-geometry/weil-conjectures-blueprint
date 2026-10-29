+++
kind = "proof"
of = "det-sbc-coefficients-adic-steps"
uses = ["sk-def-pe-derived-completion", "sk-thm-sf-ctf-stability", "sk-prop-integral-criterion", "sk-lem-sbc-exchange-compatibility", "sk-lem-pe-derived-nakayama", "sk-lem-integral-models", "sk-cor-pe-bounded-continuity", "sk-prop-scalar-six", "sk-prop-qlbar-two-colimit"]
+++
These are the three steps of [sk-prop-reduction-to-finite], spelled out for the base change map.

*Integral coefficients.* Let $\pi_E$ be the uniformizer of $\mathcal O_E$ and
$K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X$ the reductions of
[sk-def-pe-derived-completion]. By [sk-thm-sf-ctf-stability] the objects $g^*Rf_*K$ and
$Rf'_*g'^*K$ lie in $\Dbc(Y',\mathcal O_E)$, and by the integral constructibility criterion
([sk-prop-integral-criterion]) every object of $\Dbc(-,\mathcal O_E)$ is derived $\pi_E$-complete.
Since $\mathcal O_E/\pi_E^n$ has the two-term free resolution
$[\mathcal O_E\xrightarrow{\pi_E^n}\mathcal O_E]$, reduction modulo $\pi_E^n$ is the cone of
multiplication by $\pi_E^n$, so it commutes with the exact functors $Rf_*$, $Rf'_*$, $g^*$ and
$g'^*$. By its unit–counit definition, or by [sk-lem-sbc-exchange-compatibility], the reduction of
the base change map is then the base change map for the finite ring $\mathcal O_E/\pi_E^n$,

$$
 g^*Rf_*K_n\longrightarrow Rf'_*g'^*K_n.
$$

The complexes $K_n$ are bounded constructible and classical, so the finite case makes these maps
isomorphisms; already $n=1$ suffices. The cone of $g^*Rf_*K\to Rf'_*g'^*K$ is therefore derived
complete with zero reduction modulo $\pi_E$, and derived Nakayama ([sk-lem-pe-derived-nakayama]: a
derived complete complex whose reduction modulo $\pi_E$ vanishes is zero) shows that the cone is
zero. Taking $E=\Ql$ gives the case $\Zl$.

Equivalently, the integral base change map is the derived limit of the finite ones, which form a
morphism of inverse systems, under the isomorphisms

$$
 \begin{aligned}
 g^*Rf_*K&\simeq R\varprojlim_n g^*Rf_*K_n,\\
 Rf'_*g'^*K&\simeq R\varprojlim_n Rf'_*g'^*K_n.
 \end{aligned}
$$

The first holds by completeness of $g^*Rf_*K$, the second by completeness of $g'^*K$ and because the
right adjoint $Rf'_*$ preserves derived limits.

*Finite extensions $E$ of $\Ql$.* By [sk-lem-integral-models](4), every object of $\Dbc(X,E)$ is
obtained by finitely many cones and shifts from objects $K_0[1/\ell]$ with
$K_0=a_!L_0\in\Dbc(X,\mathcal O_E)$, where $a$ is a locally closed immersion and $L_0$ is lisse and
finite free. The objects on which a natural transformation of exact functors is an isomorphism are
closed under cones and shifts, so it suffices to treat $K_0[1/\ell]$. This dévissage replaces a
lattice of $K$, which may not exist. The object $K_0[1/\ell]$ is the filtered colimit of
multiplication by $\ell$ on the fixed bounded-below complex $K_0$. Inverse image commutes with this
colimit, and so do $Rf_*$ and $Rf'_*$ by continuity of cohomology ([sk-cor-pe-bounded-continuity]:
for a qcqs morphism, $R^qf_*$ commutes with filtered colimits of complexes bounded below uniformly).
These are the localization comparisons of [sk-prop-scalar-six]. By
[sk-lem-sbc-exchange-compatibility], the base change map for $K_0[1/\ell]$ is the localization of the
base change map for $K_0$, which is an isomorphism by the integral case. Taking $E=\Ql$ gives the
case $\Ql$.

*Algebraic rational coefficients.* By [sk-prop-qlbar-two-colimit], every object of $\Dbc(X,\Qlb)$ is
obtained by extension of scalars from a finite coefficient field: for $K\in\Dbc(X,\Qlb)$ there are a
finite $E\subset\Qlb$ and $K_E\in\Dbc(X,E)$ with $(K_E)_{\Qlb}\simeq K$. The comparisons of
[sk-prop-scalar-six] identify both sides and their base change map with the extension of scalars of
the base change map for $K_E$, which is an isomorphism by the previous case. Two models, or a model
and its extension to a larger finite field, become isomorphic after a common finite extension, and
[sk-lem-sbc-exchange-compatibility] identifies their base change maps there. So the isomorphism is
independent of the model.
