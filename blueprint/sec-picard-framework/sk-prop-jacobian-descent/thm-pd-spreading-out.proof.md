+++
kind  = "proof"
of    = "thm-pd-spreading-out"
+++
This is Stacks Project, Limits of Schemes, Lemma 32.10.1, Tag
[01ZM](https://stacks.math.columbia.edu/tag/01ZM); the proof is the
standard reduction to the affine case, where it is Algebra, Lemma 10.127.8,
Tag [05N9](https://stacks.math.columbia.edu/tag/05N9): a finitely
presented algebra is the colimit of its finitely generated subalgebras, and
two maps out of a finitely presented algebra agree after passing to a
sufficiently large stage. The passage from the affine case to the general
case is carried out in loc. cit. by choosing finite affine open coverings and
glueing; the three assertions are proved there in the order (3), (2), (1), and
we use them in that order. The only two notions of
[def-pc-morphism-conventions], [def-pc-base-change] that the statement needs
are ``of finite presentation'' and the fibre product $V_i\times_{S_i}S$, which
are the ones appearing in its three clauses. We record the statement here
because the chapter needs exactly those clauses, and because the generality of
the cover $\Spec(k_s)\to\Spec(k)$ is what forces this detour through a filtered
limit.
