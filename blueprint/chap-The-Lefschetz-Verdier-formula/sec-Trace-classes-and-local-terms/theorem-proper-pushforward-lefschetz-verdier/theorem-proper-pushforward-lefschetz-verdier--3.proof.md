+++
kind = "proof"
of = "theorem-proper-pushforward-lefschetz-verdier--3"
order = 925006
uses = ["definition-trace-class-local-terms", "definition-pushforward-correspondence"]
+++
For each open and closed immersion $j_i$, let $e_i$ be the natural
endomorphism of the identity functor given by the unit for $j_i^*$
and the counit for $j_i^!$, using $j_i^!\simeq j_i^*$ and
$Rj_{i!}\simeq Rj_{i*}$. The disjointness and covering hypotheses give
$\sum_i e_i=\id$ (`sum_clopenIdempotent_app`): the summands are
orthogonal, and restriction to each $B_i$ identifies the sum with
the identity.

The local term on $B_i$ is $\int_Z\alpha e_i(A_Z)$
(`BorelMooreSection.localTerm_eq_integral`). This follows by pushing
the restricted section back to $Z$ and using invariance of
integration under proper pushforward. Integration commutes with
finite sums (`BorelMooreSection.integral_sum`), hence

$$
\sum_i\operatorname{LT}_{B_i}(\alpha)
=\int_Z\alpha\Bigl(\sum_i e_i(A_Z)\Bigr)
=\int_Z\alpha.
$$

Taking $\alpha=\operatorname{Tr}_c(u)$ gives the stated specialization.
