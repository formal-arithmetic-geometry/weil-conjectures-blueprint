+++
kind = "proof"
of = "sk-thm-sf-pf-field"
uses = ["sk-cor-coefficient-heart-ii", "sk-lem-integral-models", "sk-thm-sfb-proper-base-change", "sk-lem-sf-determination", "sk-prop-proper-base-change-unbounded", "sk-prop-sf-existence"]
+++
Each claim is proved by fixing all but one variable and observing that the
objects satisfying it form a localizing subcategory containing $\Dbc$. Recall
from the construction of the localizing categories ([sk-prop-sf-existence])
that $g^*$ and $Rp_*$ for proper $p$ restrict to exact functors on
$\Loc(\Dbc(-,\Lambda))$ preserving direct sums.

*Tensor products.* Fix $B\in\Dbc(X,\Lambda)$. Since $-\otimes^{\mathbf L}B$ is
exact and preserves direct sums, the objects $A\in\Loc(\Dbc(X,\Lambda))$ with
$A\otimes^{\mathbf L}B\in\Loc(\Dbc(X,\Lambda))$ form a localizing
subcategory. It contains $\Dbc(X,\Lambda)$, because $\Dbc(X,\Lambda)$ is closed
under $\otimes^{\mathbf L}$: by [sk-cor-coefficient-heart-ii] it suffices to
treat $a_!L\otimes^{\mathbf L}b_!M$ with $L$, $M$ lisse on strata $S$, $T$,
and the formula
$(a_!L)\otimes^{\mathbf L}N\simeq a_!(L\otimes^{\mathbf L}a^*N)$ from the
proof of [sk-lem-integral-models](3) identifies it with the extension by zero
of the lisse sheaf $L\otimes M$ on $S\cap T$, and the subcategory is
everything. Now fix $A\in\Loc(\Dbc(X,\Lambda))$ and repeat the argument in
$B$.

*Projection formula.* Fix $B\in\Dbc(Y,\Lambda)$. Both sides of

$$
(Rp_*A)\otimes^{\mathbf L}B\longrightarrow Rp_*(A\otimes^{\mathbf L}p^*B)
\quad\text{in }\Loc(\Dbc(Y,\Lambda))
$$

are exact in $A$ and preserve direct sums, and the map is an isomorphism for
$A\in\Dbc(X,\Lambda)$ by [sk-thm-sfb-proper-base-change].
[sk-lem-sf-determination] extends it to all $A$. Then fix $A$ and argue in
the same way in $B$. Proper base change is
[sk-prop-proper-base-change-unbounded]. All these maps are the canonical ones
and satisfy the usual compatibilities with composition.
