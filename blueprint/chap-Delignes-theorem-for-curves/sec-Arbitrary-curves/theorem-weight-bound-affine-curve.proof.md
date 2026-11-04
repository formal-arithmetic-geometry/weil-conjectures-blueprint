+++
kind = "proof"
of = "theorem-weight-bound-affine-curve"
order = 1307
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "theorem-grothendieck-lefschetz-trace-formula", "theorem-trace-formula-euler-product", "proposition-weights-under-usual-operations", "lemma-degree-zero-top-cohomology", "lemma-boundary-stalk", "lemma-point-count-bound", "lemma-extreme-degrees-affine-curve", "lemma-cohomological-range-curve", "lemma-unramified-at-infinity-no-linear-characters", "corollary-h-1-c-stalk-fourier", "proposition-exactness-fixed-pure-weight", "lemma-finite-extension-base-field-moving", "lemma-finite-quasi-finite-direct-images"]
+++
We push the sheaf forward to the line and realize $H^1_c$ as a
quotient of a group bounded by
Theorem [theorem-weight-bound-affine-line]. This uses two
surjections. One removes the points where the direct image fails
to be lisse and pure. The other moves a lisse point to infinity.

Choose $\pi$ as in
Lemma [lemma-finite-generically-etale-map-line] and put $K=\pi_*j_!F$. Let $W_0$ be the dense
open on which $K$ is lisse and pure. Since its complement is finite,
localization gives

$$
H_c^1(W,K|_W)\twoheadrightarrow
H_c^1(\mathbf A^1,K)=H_c^1(C,F).
$$

By Lemma [lemma-finite-extension-base-field-moving], after a finite extension of
the constant field there is a further surjection from $H_c^1(V,G)$
onto $H_c^1(W,K|_W)$, with $G$ pure of weight $w$ and unramified at
infinity. Let $v:V\hookrightarrow\mathbf A^1$ be the inclusion and
$i:Z\hookrightarrow\mathbf A^1$ its finite complement. The
localization sequence for $v_*G$ reads

$$
H_c^0(Z,i^*v_*G)\longrightarrow H_c^1(V,G)
\longrightarrow H_c^1(\mathbf A^1,v_*G)\longrightarrow0.
$$

The first group has weights at most $w$ by
Proposition [proposition-weights-j-boundary-points], and the last has weights at most $w+1$ by
Theorem [theorem-weight-bound-affine-line]. As an extension of a
subgroup of the last by a quotient of the first, the middle group has
weights at most $w+1$. The bound passes to quotients under the two
surjections, and by Lemma [lemma-weight-bound-constant-extension] it holds over
the original constant field.
