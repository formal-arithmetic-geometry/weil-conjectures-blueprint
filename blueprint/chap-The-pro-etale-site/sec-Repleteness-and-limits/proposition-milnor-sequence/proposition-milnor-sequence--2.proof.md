+++
kind = "proof"
of = "proposition-milnor-sequence--2"
order = 91005
uses = ["proposition-exact-products", "proposition-milnor-sequence--1"]
+++
Apply the long exact cohomology sequence to the cone triangle (2.1).
By [proposition-exact-products], the cohomology of the product is the
product of the cohomology sheaves. Composing with each product
projection identifies the induced endomorphism with $1-T$ on these
sheaves. Factor the incoming boundary map through its cokernel and
the outgoing map through its kernel. Exactness gives a monomorphism
on the left, an epimorphism on the right, and equality of image and
kernel in the middle. The kernel of $1-T$ is the ordinary inverse
limit, since its sections are precisely compatible families.

The diagonal product map induced by a map of towers commutes with
the cone boundary and projection. The universal properties of the
kernel and cokernel therefore give both naturality squares. Finally,
compose the left inclusion with $e_1$ from
[proposition-milnor-sequence--1] to obtain (2.2), with the same right
map $b_K$.

For a homotopy limit cone in $D(\mathcal A)$, its defining
distinguished triangle has second map $1-T$ on the derived product.
Exact countable products and K-injective resolutions ensure that
cohomology preserves this product. Identify its degree-$i$
cohomology with the chosen product $P$; the projection formulas
identify the induced endomorphism with the specified $1-T$.
Factoring the boundary through its cokernel gives the left
monomorphism. In degree $j$, the kernel of $1-T$ is the chosen limit
$D$, and factoring through it gives the map induced by the cone
legs. The three adjacent exact pairs in the long exact sequence
give exactness in the middle and surjectivity on the right.
