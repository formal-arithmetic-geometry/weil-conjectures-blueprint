+++
kind  = "proof"
of    = "lem-sfb-lc-weakly-etale"
+++
A locally constant function on the compact space $S$ takes finitely many
values. It therefore factors through a finite quotient of $S$. Let $S_i$ run
over the finite quotients of $S$; they form a cofiltered system. Then
$$
LC(S,\Z)=\colim_i\Z^{S_i}
$$
is a filtered colimit of finite products of copies of $\Z$.

Each $\Z^{S_i}$ is flat over $\Z$. The multiplication map
$\Z^{S_i}\otimes_\Z\Z^{S_i}=\Z^{S_i\times S_i}\to\Z^{S_i}$ is the projection
onto the diagonal factor, so it is flat as well. Flatness passes to filtered
colimits of ring maps. Moreover, tensor products commute with filtered
colimits. Hence $LC(S,\Z)$ is flat over $\Z$, and the multiplication map
$LC(S,\Z)\otimes_\Z LC(S,\Z)\to LC(S,\Z)$ is flat. This is the definition of
weakly étale.
