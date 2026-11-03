+++
kind  = "proof"
of    = "det-thm-sfb-proper-base-change-rational"
+++
(1) $K[1/\ell]=\varinjlim(K\xrightarrow{\ell}K\to\cdots)$ termwise, a filtered system with a common
lower bound; $R^qp_*$ commutes with it by [sk-cor-pe-bounded-continuity] ($p$ is qcqs). So the
canonical map $(Rp_*K)[1/\ell]\to Rp_*(K[1/\ell])$ is an isomorphism on cohomology sheaves. For a
finite $F/E$, $F_X\cong E_X^{[F:E]}$ as $E_X$-modules
([det-prop-sfb-cartesian-coefficients-finite-free]), compatibly with pullback, so $K_F$ is a
finite direct sum of copies of $K$ and $Rp_*$ commutes with it. For $\Qlb$, write
$K_{\Qlb}=\varinjlim_FK_F$, again a bounded below filtered colimit, and apply
[sk-cor-pe-bounded-continuity].

(2) By [det-lem-integral-models-generators], $\Dbc(X,E)$ is generated under finitely many
cones and shifts by $(a_!L_0)[1/\ell]$ with $a_!L_0\in\Dbc(X,\cO_E)$, and $\Dbc(X,\Qlb)$ by
$(a_!L_0)_{\Qlb}$. By (1) and the integral case
([det-thm-sfb-proper-base-change-integral] (1)), $Rp_*$ of a generator is $(Rp_*a_!L_0)[1/\ell]$,
resp. $(Rp_*a_!L_0)_{\Qlb}$, with $Rp_*a_!L_0\in\Dbc(Y,\cO_E)$; extension of scalars preserves
$\Dbc$ (it is exact and preserves lisse-on-strata). Since $Rp_*$ is exact and $\Dbc(Y,\Lambda)$ is
triangulated ([det-cor-coefficient-heart-ii-triangulated]), $Rp_*$ preserves $\Dbc$.

(3) The class of $K$ (resp. pairs $(K,M)$) for which the canonical map is an isomorphism is
closed under cones and shifts in each variable, since all functors are exact and the maps are
natural transformations of exact functors (five lemma). On generators, the maps are the
rationalizations, resp. scalar extensions, of the integral canonical maps (by (1) and the
compatibility of $g^*$, $\otimes^{\mathbf L}$ with $[1/\ell]$ and scalar extension, which hold since
these functors commute with colimits), and those are isomorphisms by
[det-thm-sfb-proper-base-change-integral] (3). Dévissage in each variable concludes.
