+++
kind = "proof"
of = "proposition-properties-trace--4"
order = 895011
uses = ["definition-categorical-trace", "proposition-properties-trace--3"]
+++
The degree-zero coevaluation is the sum of its components in
$P^i\otimes(P^\vee)^{-i}$ for $a\le i\le b$. Distribute the trace
composite over this sum. The Koszul braiding on the $i$th component
contributes $(-1)^{i(-i)}=(-1)^i$, and the remaining evaluation and
coevaluation composite is the trace of $v^i$. This proves the first
formula; the identification of a summand is
`CochainComplex.rightDual.coevPQ_comp_evalPQ`.

For the second formula, dualizable objects are flat, so the bounded
complex $P^\bullet$ and its termwise dual are K-flat. First transport
their exact pairing to the homotopy category, then lift it to the full
subcategory of K-flat objects. Localization is strong monoidal on this
subcategory. Apply trace functoriality as in
[proposition-properties-trace--3], using the assumed compatibility of
the braidings. The unit comparison gives the two factors $\epsilon$
and $\epsilon^{-1}$, and independence of the right dual allows the
specified dual in the derived category. For the standard derived
braiding the compatibility is `DerivedCategory.braiding_hom_μ_Qh`.
