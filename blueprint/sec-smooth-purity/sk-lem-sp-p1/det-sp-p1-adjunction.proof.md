+++
kind = "proof"
of = "det-sp-p1-adjunction"
uses = ["det-sp-p1-trace", "thm-amb-p1-adjunction", "sk-prop-sp-et-proet"]
+++
*First identity.* Using composition of direct images, $qp_1=qp_2$, proper base
change and the projection formula, the composite
$\varepsilon_{Rq_*M}\circ Rq_*(\eta_M)$ equals

$$
Rq_*M=R(qp_1)_*\Delta_*M\to R(qp_1)_*p_1^*M(1)[2]
\simeq Rq_*\bigl(M\otimes^{\mathbf L}Rp_{1*}(\Lambda_n)(1)[2]\bigr)
\xrightarrow{Rq_*(1_M\otimes\operatorname{Tr}_{p_1})}Rq_*M .
$$

The proper base-change map is the adjoint transpose of the counit of
$g^*\dashv Rg_*$ for the relevant pullback, and the projection map is the
adjoint transpose of tensoring with the same counit; expanding these
definitions along either route uses this counit once in each coordinate, in
the same order once $qp_1=qp_2$ is used. Hence the first arrow is
$1_M\otimes Rp_{1*}\delta$ under the projection identification, and the
composite is $Rq_*(1_M\otimes(\operatorname{Tr}_{p_1}\circ Rp_{1*}\delta))=Rq_*(1_M)$
by [det-sp-p1-trace] (3).

*Second identity.* For $M=q^*K(1)[2]$, $p_1^*M$ and $p_2^*M$ both equal
$(qp_1)^*K(1)[2]=(qp_2)^*K(1)[2]$, since $K$ and the twist come from $S$. The
projection formula takes this common factor outside $Rp_{2*}$, and
$q^*(\varepsilon_K)(1)[2]$ contracts the remaining kernel by
$\operatorname{Tr}_{p_2}$; so the composite is
$1_{q^*K(1)[2]}\otimes(\operatorname{Tr}_{p_2}\circ Rp_{2*}\delta)=1$ by
[det-sp-p1-trace] (3). All shifts moved are even, so no Koszul signs appear.

*Adjunction and base change.* Two natural transformations satisfying the
triangle identities exhibit an adjunction ([thm-amb-p1-adjunction]). The unit
is built from $\delta$ (compatible with base change, $\Delta$ being a relative
Cartier divisor in every fibre) and proper base change; the counit from
$\operatorname{Tr}_q$ and the projection formula; all are compatible with base
change on $S$, hence so are $\eta$ and $\varepsilon$.

*Restriction to $\Dctf$.* $Rq_*$ preserves $\Dctf$ (proper direct image), and
$q^*(-)(1)[2]$ preserves $\Dctf$ (inverse image, twist by an invertible sheaf,
shift). The comparison of [sk-prop-sp-et-proet] transports the étale adjunction
to the pro-étale categories, Hom groups agreeing by full faithfulness.
