+++
kind = "proof"
of = "sk-thm-dl-general-sheaf"
uses = ["sk-lem-wgen-triangle-weights"]
+++
We first show that the asserted property is stable under composition.
For $X_0\xrightarrow{h}Z_0\xrightarrow{g}Y_0$, consider the Leray
spectral sequence for compact supports,

$$
E_2^{a,b}=R^ag_!(R^bh_!F)\ \Longrightarrow\ R^{a+b}(gh)_!F.
$$

It is Frobenius-equivariant by the naturality of the truncation tower
and of the composition isomorphism for direct image with proper
support. If both maps have the asserted property, then $E_2^{a,b}$ is
mixed of weights at most $w+a+b$. Each later page is a subquotient of
the previous one, so the same holds for $E_\infty^{a,b}$. The abutment
filtration of $R^n(gh)_!F$ is finite, because the operations preserve
bounded constructible complexes, and its quotients are the
$E_\infty^{a,n-a}$. Hence $R^n(gh)_!F$ is mixed of weights at most
$w+n$ by Lemma [sk-lem-wgen-triangle-weights].

Now we apply Lemma [sk-l-dl-general-normalization] and refine the
partitions to filtrations by open and closed pieces. The restriction
of $F$ to each source piece is again mixed of weights at most $w$. On
every refined source piece, the finite map to $\mathbf A^d_V$ restricts
to a separated quasi-finite map, and hence it has the property by
Lemma [sk-l-dl-general-quasifinite]. The projection $\mathbf A^d_V\to V$ is a
composition of $d$ projections of relative affine lines, each of which
has the property by Proposition [sk-prop-wgen-relative-line]. By the
composition argument, the map from the piece to $V$ has the property.
The localization sequences on the source, base change on the target
and Lemma [sk-lem-wgen-triangle-weights] then give the bound for
$R^if_!F$ on $Y_0$.
