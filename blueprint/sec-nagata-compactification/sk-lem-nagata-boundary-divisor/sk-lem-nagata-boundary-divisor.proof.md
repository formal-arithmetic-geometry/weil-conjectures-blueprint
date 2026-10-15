+++
kind  = "proof"
of    = "sk-lem-nagata-boundary-divisor"
uses = ["sk-def-nagata-admissible"]
+++
Choose a finite-type quasi-coherent ideal $\mathcal I$ with
$V(\mathcal I)=T\setminus U$; such an ideal exists for a quasi-compact open in
a qcqs scheme (Stacks 01PH). Blow up this ideal. The transformed ideal defines
the exceptional Cartier divisor. On its affine charts the local defining
element $a$ is a nonzerodivisor, so the map from the chart ring to its
localization at $a$ is injective. The complement of the divisor is
consequently schematically dense. It is precisely the inverse image of $U$.

This density persists under subsequent admissible blow-ups. Locally, if $t$
defines the boundary divisor, multiplication by $t$ is injective on each
power of a blow-up ideal, since those powers are submodules of
$\mathcal O_T$. It is therefore injective on the Rees algebra and its
degree-zero localized charts. The pulled-back $t$ still defines a Cartier
divisor with complement the inverse image of $U$.
