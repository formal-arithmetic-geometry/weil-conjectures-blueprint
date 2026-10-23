+++
kind  = "proof"
of    = "lem-exc-proetale-closed-fully-faithful"
+++
First let $X=\operatorname{Spec}A$ and $Z=\operatorname{Spec}(A/I)$. On the
affine ind-etale bases, base change $u$ to $Z$ is right adjoint to the
closed-site lift $v$ with invertible unit $\operatorname{id}\to uv$
([lem-exc-closed-site-adjunction]). Passing to opposite categories and
precomposing, precomposition with $u$ is therefore fully faithful on
presheaves of $R$-modules: its adjoint has an invertible counit, given at a
presheaf $F$ by $F$ applied to the unit of $v\dashv u$. Restriction of sheaves
to these bases is an equivalence, and on the bases the direct image $i_*$ is
precomposition with $u$, so $i_*$ is fully faithful. An arbitrary closed
immersion into an affine scheme is isomorphic to such a quotient immersion,
and direct images compose, so $i_*$ is fully faithful whenever $X$ is affine;
equivalently the counit is an isomorphism.

In general, cover $X$ by affine opens $X_k$ and put $Z_k=Z\times_XX_k$. The
restrictions to the $Z_k$ form a pro-etale cover of $Z$, so a map of sheaves on
$Z$ is an isomorphism once its restrictions to all $Z_k$ are. By
[lem-exc-closed-localization], applied to the cartesian squares formed by the
open immersions $X_k\to X$, $Z_k\to Z$ and the closed immersions, restriction
to $Z_k$ carries the counit of $i^*\dashv i_*$ to the counit for
$Z_k\hookrightarrow X_k$, up to isomorphism. These affine counits are
isomorphisms by the first step, so the global counit is an isomorphism. An
adjunction has fully faithful right adjoint precisely when its counit is an
isomorphism, giving the assertion.
