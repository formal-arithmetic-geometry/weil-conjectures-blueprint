+++
kind  = "proof"
of    = "lem-sp-shift-identification"
+++
The derived functor of a left exact additive functor
[def-sp-left-exact-additive] on $\operatorname{Ch}^+$ is the functor applied
to a K-injective resolution, by the definition in
[def-sp-kinjective-bridge]. It commutes with the shift by part (3) of
[lem-sp-kinjective-computes], so the cohomology of the shifted complex is the
shifted cohomology, which is the displayed isomorphism; it is natural in $K$
because both steps are. For $p\geq0$ the identification with
$R^pv(\mathcal H^q(K))$ is the
definition $R^pv=\mathcal H^p\circ Rv$ of [def-sp-kinjective-bridge],
together with part (2) of [lem-sp-kinjective-computes] identifying it, on an
object, with the derived functor of [def-sp-left-exact-additive].
For $p<0$ the object $\mathcal H^qK$ placed in degree $0$ has no cohomology in
negative degrees, so $\mathcal H^p(Rv(\mathcal H^qK))=0$ by
[lem-weil-pbc-derived-functor-negative-vanishing], and the displayed isomorphism
transports this vanishing to $\mathcal H^{p+q}(Rv(\mathcal H^qK[-q]))$.
