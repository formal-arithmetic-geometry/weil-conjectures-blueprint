+++
kind = "proof"
of = "det-thm-sf-pf-field-tensor"
+++
(1) By [sk-cor-coefficient-heart-ii], $\Dbc(X,\Lambda)$ is the smallest
triangulated subcategory containing the objects $a_!L$, where
$a:S\hookrightarrow X$ is the inclusion of a locally closed stratum and $L$ is
a lisse sheaf on $S$. Since $-\otimes^{\mathbf L}-$ is exact in each variable,
the objects $K$ with $K\otimes^{\mathbf L}N\in\Dbc$ for all $N\in\Dbc$ form a
triangulated subcategory, so it suffices to show
$a_!L\otimes^{\mathbf L}b_!M\in\Dbc(X,\Lambda)$ for strata $a:S\hookrightarrow X$,
$b:T\hookrightarrow X$ and lisse $L$, $M$. For a locally closed immersion $a$
and any $N$ there is a natural isomorphism
$(a_!L)\otimes^{\mathbf L}N\simeq a_!(L\otimes^{\mathbf L}a^*N)$ (proof of
[sk-lem-integral-models](3): it holds for open immersions and closed
immersions on stalks, hence for composites). With $N=b_!M$, base change for
extension by zero gives $a^*b_!M\simeq c_!(M|_{S\cap T})$ with
$c:S\cap T\hookrightarrow S$, and applying the formula once more,
$a_!L\otimes^{\mathbf L}b_!M\simeq(ac)_!(L|_{S\cap T}\otimes M|_{S\cap T})$.
The tensor product of two lisse sheaves is lisse (it is locally a tensor of
finite free modules, which is flat, so the derived tensor is underived), and
extension by zero of a lisse sheaf on a locally closed subset is in $\Dbc$.

(2) Fix $B\in\Dbc(X,\Lambda)$. The functor $-\otimes^{\mathbf L}B$ on
$D(X_{\mathrm{proét}},\Lambda)$ is exact and preserves direct sums, so the full
subcategory of $A\in\Loc(\Dbc(X,\Lambda))$ with
$A\otimes^{\mathbf L}B\in\Loc(\Dbc(X,\Lambda))$ is closed under shifts, cones
and direct sums, i.e. localizing. By (1) it contains $\Dbc(X,\Lambda)$, hence
it is all of $\Loc(\Dbc(X,\Lambda))$. Now fix $A\in\Loc(\Dbc(X,\Lambda))$; by
what was just shown, the objects $B$ with
$A\otimes^{\mathbf L}B\in\Loc(\Dbc(X,\Lambda))$ form a localizing subcategory
containing $\Dbc(X,\Lambda)$, hence everything.
