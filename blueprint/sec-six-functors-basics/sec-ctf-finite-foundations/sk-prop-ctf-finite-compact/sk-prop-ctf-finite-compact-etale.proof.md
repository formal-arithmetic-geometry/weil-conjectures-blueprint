+++
kind = "proof"
of = "det-ctf-finite-compact-etale"
+++
*Generators.* By [sk-lem-sf-flat-model] (étale form), $\Dctf(X_{\mathrm{ét}},A)$ is generated under shifts,
finite extensions and direct summands by sheaves $a_!L$, with $a\colon S\hookrightarrow X$ locally closed and
$L$ locally constant with finite projective local models. The compact objects of a triangulated category
with sums form a thick subcategory (five lemma for cones; a summand of a compact object is compact since
the comparison map for it is a retract of an isomorphism). So it suffices to treat $C=a_!L$.

*Formula.* Write $a=i\circ u$ ($i\colon Z\hookrightarrow X$ closed, $u\colon S\hookrightarrow Z$ open) and let
$j\colon X\setminus Z\hookrightarrow X$ be the complement. $L$ is dualizable with dual
$L^\vee=\underline{\operatorname{Hom}}_A(L,A_S)$, so $L\otimes-$ has right adjoint $L^\vee\otimes-$. Using
$a_!=i_*u_!$, $u_!\dashv u^*$, $i_*\dashv R\underline\Gamma_Z$ (étale form of part (1) of
[sk-lem-formal-closed-support]) and $\Hom(L\otimes A_S,M)=\Hom(A_S,L^\vee\otimes M)$:

$$
R\operatorname{Hom}_X(a_!L,K)=R\operatorname{Hom}_S(L,u^*R\underline\Gamma_ZK)=R\Gamma\bigl(S,L^\vee\otimes_Au^*R\underline\Gamma_ZK\bigr),
\qquad R\underline\Gamma_ZK=i^*\fib(K\to Rj_*j^*K).
$$

*Sums.* Each functor in $K\mapsto R\Gamma(S,L^\vee\otimes u^*i^*\fib(K\to Rj_*j^*K))$ preserves arbitrary
direct sums of unbounded complexes: $j^*$, $i^*$, $u^*$ are left adjoints; $L^\vee\otimes-$ is a left adjoint;
fibers commute with sums; and $Rj_*$, $R\Gamma(S,-)$ have finite cohomological dimension on $\ell$-primary
torsion sheaves in our setting, so they commute with direct sums of unbounded complexes ([Stacks, Tag 0F11](https://stacks.math.columbia.edu/tag/0F11)), for $A$-modules because derived direct image and global sections commute with forgetting the
coefficient ring ([Stacks, Tag 0D6J](https://stacks.math.columbia.edu/tag/0D6J)). Hence
$R\operatorname{Hom}(a_!L,\bigoplus K_s)=\bigoplus R\operatorname{Hom}(a_!L,K_s)$, and taking $H^0$ gives
$\Hom(a_!L,\bigoplus K_s)=\bigoplus\Hom(a_!L,K_s)$ (cohomology of complexes of abelian groups commutes with
sums).
