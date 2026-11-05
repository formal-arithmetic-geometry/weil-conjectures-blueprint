+++
kind = "proof"
of = "lemma-bounds-squared-traces--4"
order = 1202010
uses = ["definition-growth-squared-traces"]
+++
For $\beta>B-1$, the assumed estimate gives

$$
\frac{S_n(F)}{q^{n(\beta+1)}}
\le Cq^{n(B-\beta-1)}\longrightarrow0.
$$

The ratios are nonnegative, so their upper limit is zero. In Lean's
supremum formulation of [definition-growth-squared-traces], no such
$\beta$ contributes to $\nu(F)$; hence $\nu(F)\le B-1$.
