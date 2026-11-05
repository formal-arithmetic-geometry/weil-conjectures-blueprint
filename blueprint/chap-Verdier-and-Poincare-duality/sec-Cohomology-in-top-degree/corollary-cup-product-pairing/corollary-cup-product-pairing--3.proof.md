+++
kind = "proof"
of = "corollary-cup-product-pairing--3"
order = 871006
uses = ["corollary-cup-product-pairing--2"]
+++
Apply [corollary-cup-product-pairing--2] with $i=j=d$ and $b=a$.
Since $d$ is odd, $\langle a,a\rangle=-\langle a,a\rangle$.
Thus $2\langle a,a\rangle=0$, and $\Qbarl$ has characteristic zero,
so $\langle a,a\rangle=0$. This is the informal consequence retained
here; the Lean proof of the main theorem does not invoke it.
