+++
kind = "proof"
of = "corollary-evaluation-weakly-contractible-objects--7"
order = 79015
uses = ["definition-ind-etale-pro-etale-weakly--1", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--7", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "definition-w-local-w-strictly-local--4", "theorem-existence-contractible-covers--1", "lemma-w-contractible-affines-projective--1"]
+++
If $f$ is an isomorphism, so is every $f(W)$. Conversely, suppose that every
$f(W)$ is bijective. Apply clause [corollary-evaluation-weakly-contractible-objects--6] to the sequence
$0\to A\xrightarrow{f}B$. On every affine weakly contractible $W$ the sequence
$0\to A(W)\to B(W)$ is exact because $f(W)$ is injective, so the sequence is
exact at $A$, that is, $f$ is a monomorphism. Apply clause [corollary-evaluation-weakly-contractible-objects--6]
to $A\xrightarrow{f}B\to0$. On every such $W$ it is exact at $B(W)$ because
$f(W)$ is surjective, so $f$ is an epimorphism. In the abelian category of
$\mathcal R$-module sheaves a monomorphism that is an epimorphism is an
isomorphism.

For complexes, let $C=\Cone(v)$, with $C^q=K^{q+1}\oplus L^q$ and the usual
differential. The termwise split exact sequence $0\to L\to C\to K[1]\to0$
gives a long exact cohomology sequence whose connecting maps are, up to sign,
the maps $H^q(v)$. Hence $v$ is a quasi-isomorphism if and only if $C$ is
acyclic. Evaluation at $W$ is additive and commutes with the differentials,
so $C(W)$ is the cone of $v(W)$, and in the same way $v(W)$ is a
quasi-isomorphism if and only if $C(W)$ is acyclic. By the second assertion
of clause [corollary-evaluation-weakly-contractible-objects--6], $C$ is acyclic if and only if $C(W)$ is acyclic
for every affine weakly contractible $W$. This proves the assertion for
complexes, again without any boundedness assumption.

*Source:* the proof of Corollary [corollary-evaluation-weakly-contractible-objects].
