+++
kind = "proof"
of = "sk-prop-sf-open-closed-triangle"
uses = ["sk-def-sf-operations"]
+++
The key limit assertion is local on $X$. A weakly contractible affine test
object $V$ in the affine ind-étale basis of $Z$ has a canonical henselian
lift $v(V)$ in the corresponding basis of $X$: the functor $v$ is the fully
faithful left adjoint to base change of these affine bases, and
$v(V)\times_XZ\simeq V$ (Stacks, Tag 09A9, Lemmas 61.25.1–61.25.2). The
pullback of a sheaf, evaluated on $V$, is its evaluation on $v(V)$, because
no sheafification is needed on a weakly contractible object. Evaluation
commutes with limits and these test objects detect isomorphisms, so $i^*$
preserves limits. As a left adjoint it preserves colimits, and it is exact.
Lifting covers through the henselian thickenings proves exactness of $i_*$
and the identities $i^*i_*=\mathrm{id}$ and $j^*i_*=0$. The open–closed
sequence follows by the same cover descent, or from its kernel description.

On derived categories this gives, for $K\in D(U_{\mathrm{proét}},j^*B)$, the
triangle

$$
j_!K\longrightarrow Rj_*K\longrightarrow i_*i^*Rj_*K\longrightarrow j_!K[1]
\quad\text{in }D(X_{\mathrm{proét}},B).
$$

Its last two terms preserve products and derived inverse limits, hence so
does their fibre $j_!$. Exactness and exact products give the corresponding
limit statements on module sheaves. This is the henselian-thickening
argument of Bhatt–Scholze, §6.1; see also Stacks, Tags 09AA, 09AH, 09BM and
09BP.
