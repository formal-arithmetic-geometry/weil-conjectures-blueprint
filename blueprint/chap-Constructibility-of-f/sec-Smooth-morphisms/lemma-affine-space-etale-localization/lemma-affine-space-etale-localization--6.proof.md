+++
kind = "proof"
of = "lemma-affine-space-etale-localization--6"
order = 558013
+++
(2) For an étale $u$, the functor $Ru_!$ is extension by zero. By its
elementary construction [Stacks, [03S2](https://stacks.math.columbia.edu/tag/03S2)], it is an exact functor
$u_!:\operatorname{Mod}(U_{\acute{e}t},\Lambda)\to\operatorname{Mod}(X_{\acute{e}t},\Lambda)$ left adjoint to $u^*$.
As both functors are exact, they need not be derived, and the adjunction
extends to derived categories. For every $M\in D(U_{\acute{e}t},\Lambda)$,

$$
\Hom(M,u^*f^!N)
=\Hom(u_!M,f^!N)
=\Hom(Rf_!u_!M,N)
=\Hom(R(fu)_!M,N),
$$

where the last step is the composition isomorphism of [Stacks, [0F7J](https://stacks.math.columbia.edu/tag/0F7J)]. The
Yoneda lemma gives (6.12). Taking $M=u^*f^!N$ and the
identity on the left, we see that the counit of $R(fu)_!\dashv(fu)^!$ is
the composite of the counits as stated. The isomorphism for $uu'$ and the
composite of those for $u$ and $u'$ both correspond under the Yoneda lemma
to bijections obtained from the composition isomorphism for
$f\circ u\circ u'$. These bijections agree by associativity of the
composition isomorphisms [Stacks, [0F7K](https://stacks.math.columbia.edu/tag/0F7K)].

*Source:* the proof of Lemma [lemma-affine-space-etale-localization].
