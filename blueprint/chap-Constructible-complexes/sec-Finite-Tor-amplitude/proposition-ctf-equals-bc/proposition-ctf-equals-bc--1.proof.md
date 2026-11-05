+++
kind = "proof"
of = "proposition-ctf-equals-bc--1"
order = 252002
uses = ["definition-constructible-sheaves"]
+++
Fix a sheaf $N$ of $\Lambda_X$-modules. Derived tensor with $N$ commutes
with shifts, so the hypothesis on $H^q(K)$ gives Tor amplitude
$[q+c,q+d]$ for $H^q(K)[-q]$. For $a\leq q\leq b$, this interval is
contained in $[a+c,b+d]$.

Zero has Tor amplitude in this interval, and the condition is invariant
under isomorphism and closed under extensions: tensor a distinguished
triangle with $N$ and use the long exact sequence in cohomology. Apply
these facts successively to the canonical truncation triangles

$$
\tau_{\leq q-1}K\longrightarrow\tau_{\leq q}K
\longrightarrow H^q(K)[-q]\longrightarrow(\tau_{\leq q-1}K)[1].
$$

Since $\tau_{\leq a-1}K=0$ and $\tau_{\leq b}K\simeq K$, finite
induction proves that $K\otimes^{\mathbf L}_{\Lambda_X}N$ has cohomology
only in $[a+c,b+d]$. This holds for every $N$, which is the required
Tor bound in Definition [definition-constructible-sheaves].
