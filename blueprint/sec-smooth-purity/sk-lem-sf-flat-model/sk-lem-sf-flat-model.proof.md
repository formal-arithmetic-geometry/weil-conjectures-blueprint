+++
kind  = "proof"
of    = "sk-lem-sf-flat-model"
+++
*(ii)$\Rightarrow$(i):* a bounded-above complex of flat sheaves is
K-flat, and $P\otimes_AM$ has terms only in degrees $[a,b]$.
*(i)$\Rightarrow$(ii):* choose a bounded-above free resolution
$P\to K$; testing with $M=A_T$ gives $H^q(P)=0$ for $q<a$; put
$Q=P^a/\mathrm{im}(P^{a-1}\to P^a)$ and compute
$\mathrm{Tor}^A_1(Q,M)=H^{a-1}(P\otimes_AM)=H^{a-1}(K\otimes^L_AM)=0$, so $Q$
is flat by the Tor form of the finite-relation criterion; then
$P'=[Q\to P^{a+1}\to\dots\to P^b]$ is the required model.
*Constructible variant:* build the bounded-above resolution $P\to K$
inductively in decreasing degree with terms finite direct sums of
$j_{V!}A_V$: the surjections needed at each step are onto the constructible
cohomology sheaves of $K$ and onto the constructible kernels and cokernels
that arise, and they exist by the key input, after refining each $V$ by a
finite affine étale cover so that the relevant sections lift
(SGA $4\frac12$, Rapport, 4.6–4.8). Then $Q=P^a/\mathrm{im}(P^{a-1}\to
P^a)$ is a cokernel of a map of constructible sheaves, hence constructible as
well as flat, and $P'$ is a bounded complex of flat constructible sheaves.
