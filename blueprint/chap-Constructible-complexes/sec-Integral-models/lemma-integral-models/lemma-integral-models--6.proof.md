+++
kind = "proof"
of = "lemma-integral-models--6"
order = 294007
uses = ["lemma-integral-models--5", "lemma-lattices-after-finite-stratification", "lemma-continuity-ext-out-constructible-complex"]
+++
First give each constructible cohomology sheaf an integral model. On each
stratum the rational sheaf is locally free after refinement and admits a
constructible integral lattice. Extension by zero and a finite filtration
by closed subsets reconstruct the sheaf from these pieces.

The essential image of integral scalar extension is triangulated.
Indeed, continuity of Ext identifies rational morphisms with integral
morphisms after inverting $\ell$. Multiply a morphism by a power of $\ell$
to lift it integrally, and take its integral cone. Multiplication by that
power is invertible after scalar extension, so the cone rationalizes to
the required rational cone. Shifts are preserved as well.

Finally apply induction through the bounded truncation triangles of $K$.
Their cohomology terms already have integral models, and triangulated
closure supplies a model of $K$. This proves existence of the whole
integral complex; Lean does not use the original assertion that the
specified locally free lattice extensions generate the category.
