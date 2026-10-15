+++
kind = "proof"
of = "det-prop-p1-adjunction-rational-triangle"
+++
The calculation in the proof of [sk-prop-geo-p1-adjunction] for torsion
coefficients uses only three kinds of identification: the projection formula
for proper morphisms, proper base change, and the composition isomorphisms
$R(gh)_*\simeq Rg_*Rh_*$, each applied to the canonical maps and used with
their standard compatibilities (naturality, compatibility with composition
of squares, and compatibility of the projection formula with the base change
map). On the categories $\Loc(\Dbc(-,\Lambda))$ these hold by
[sk-thm-sf-pf-field], and composition of direct images holds on the ambient
derived categories. So the calculation goes through verbatim; we recall its
shape.

*First identity.* In $\varepsilon_{Rq_*M}\circ Rq_*(\eta_M)$, write
$Rq_*Rp_{2*}=R(qp_2)_*=R(qp_1)_*=Rq_*Rp_{1*}$. The projection formula for
$p_1$ moves the factor $M$ outside:
$Rp_{1*}(p_1^*M\otimes^{\mathbf L}N)\simeq M\otimes^{\mathbf L}Rp_{1*}N$. The base
change map in $\eta$ is defined by the counit of $p_1^*\dashv Rp_{1*}$, and
under these identifications it cancels against the restriction to the
diagonal, $Rp_{1*}\Delta_*=\mathrm{id}$. The trace in $\varepsilon$ becomes,
under base change, $\operatorname{Tr}_{p_1}$. What remains is
$Rq_*$ of $1_M$ tensored with the endomorphism
$\operatorname{Tr}_{p_1}\circ Rp_{1*}\delta_\Lambda$ of $\Lambda_{\mathbf P^1_Y}$
(identified via the projection formula for $p_1$).

*Second identity.* Symmetrically, for $M=q^*K(1)[2]$ the factor $q^*K$ is
moved outside $Rp_{2*}$ by the projection formula for $p_2$, the base change
map cancels against $Rp_{2*}\Delta_*=\mathrm{id}$, and what remains is
$1_{q^*K(1)[2]}$ tensored with
$\operatorname{Tr}_{p_2}\circ Rp_{2*}\delta_\Lambda$.

By the integration identities of [sk-prop-diagonal-tower],
$\operatorname{Tr}_{p_i}\circ Rp_{i*}\delta_\Lambda=1$ for $i=1,2$. Hence both
composites are identities: these are the triangle identities, and
$(\eta,\varepsilon)$ exhibits $q^*(1)[2]$ as right adjoint to $Rq_*$ on the
localizing categories. Since $q$ is proper, $Rq_!=Rq_*$ there (trivial
compactification), and $q^!$ is by definition a right adjoint of $Rq_!$
([sk-prop-sf-existence]). Right adjoints are unique up to unique isomorphism
compatible with the counits, so $q^!\simeq q^*(1)[2]$.
