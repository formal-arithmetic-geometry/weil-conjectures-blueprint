+++
kind  = "proof"
of    = "thm-exc-explicit-preservation"
+++
By [prop-exc-open-adjoint], [prop-exc-finite-etale-adjoint], the ambient
right adjoint is the exact functor $f^*$. Pull back each stratum in
[def-weil-finite-torsion-constructibility]. The resulting partition
is finite and constructible; inverse image of a locally constant finite
module sheaf is locally constant with the same finite module fibres.
Exactness identifies $\mathcal H^q(f^*K)$ with
$f^*\mathcal H^q(K)$, proving the assertion about the intervals of
[def-weil-constructible-intervals].

If $K$ has Tor amplitude $[a,b]$, the usual flat-resolution
criterion for [def-weil-finite-tor-amplitude] represents it by a
complex of flat module sheaves in these degrees. Inverse image preserves
flatness: the relations criterion for flatness is local and is preserved
by the exact inverse-image functor and its compatibility with tensor
products. Pulling back this bounded flat complex and tensoring it with
any module sheaf on $V$ proves the same Tor bound. Finally inverse
image is an exact tensor functor and preserves flat resolutions. Applying
it to a flat resolution in the definition of the derived tensor product
in [def-weil-derived-tensor] gives the displayed coefficient
isomorphism. No assertion that $A\to B$ is flat is used.
