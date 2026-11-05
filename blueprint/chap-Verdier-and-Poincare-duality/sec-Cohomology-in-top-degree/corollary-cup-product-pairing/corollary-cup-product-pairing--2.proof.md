+++
kind = "proof"
of = "corollary-cup-product-pairing--2"
order = 871005
uses = []
+++
Expand the pairing as the trace of a cup product. Graded commutativity
and linearity of the trace give
$\langle b,a\rangle=(-1)^{ij}\langle a,b\rangle$; this is
`FrobeniusModule.TraceCup.pairing_comm`. Since $j=2m-i$,

$$
ij-i=2mi-i(i+1)
$$

is even. Hence $(-1)^{ij}=(-1)^i$, which gives the assertion.
