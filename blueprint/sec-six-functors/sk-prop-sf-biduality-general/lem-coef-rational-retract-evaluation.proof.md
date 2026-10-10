+++
kind  = "proof"
of    = "lem-coef-rational-retract-evaluation"
+++
If $i:P\to K$, $p:K\to P$ satisfy $pi=1$, then
$D(p):DP\to DK$, $D(i):DK\to DP$ are a splitting
of $D(ip)$. Naturality of the isomorphism $\delta$ in
[thm-coef-rational-verdier] identifies its restriction on
this summand with $\delta_P$. The restricted evaluation is

$$
DP\otimes P\xrightarrow{D(p)\otimes i}DK\otimes K
\longrightarrow\omega.
$$

Its equality with evaluation for $P$ follows by tensor–Hom
naturality and $pi=1$. For a general pairing in the
statement, the two adjoint isomorphisms intertwine the specified
idempotents, and hence induce isomorphisms between their images.
This proves the assertion about the restricted pairing.
The comparisons of [lem-coef-integral-finite-extension],
rationalized, carry these maps and splittings to the ones after
finite scalar extension. Exact functors preserve isomorphisms,
so they preserve the asserted property.

No enlargement of the coefficient categories is involved:
[lem-weil-rationalization-idempotent-complete], [lem-weil-qbar-idempotent-complete]
already supplies the splittings. For a site-perfect complex in
[def-weil-site-perfect-complex], the tensor-dual evaluation
is locally the evaluation of a bounded finite-projective complex.
Tensor extension and passage to a direct summand preserve that
calculation. This last statement concerns the tensor dual to
the unit; the preceding Verdier evaluation uses $\omega$ and
does not assert that every constructible complex is site-perfect.
