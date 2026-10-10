+++
kind  = "proof"
of    = "lem-weil-derived-tensor-functorial"
+++
On the small pro-etale site [def-weil-pbc-proetale-site], choose
K-flat resolutions $P\to K_1$ and $P'\to K_1'$, so that
$K_1\otimes_A^LK_2=P\otimes_AK_2$ and $K_1'\otimes_A^LK_2'=P'\otimes_AK_2'$
by [def-weil-derived-tensor]. For a morphism $K_2\to K_2'$ the ordinary
tensor product $P\otimes_A-$ is functorial and the result is independent of
the resolution $P\to K_1$ by
[lem-weil-derived-tensor-resolution-independent]. For a morphism $K_1\to
K_1'$, the composite $P\to K_1\to K_1'$ factors, up to homotopy, through a
morphism of complexes $P\to P'$ which is well defined in the homotopy
category (Lemma 15.60.16 of the Stacks Project, Tag
[0G6M](https://stacks.math.columbia.edu/tag/0G6M)); tensoring it with $K_2$
and applying [lem-weil-derived-tensor-resolution-independent] once more gives
the induced morphism, again independently of the resolutions. Compatibility
with identities and composition is inherited from the ordinary tensor product
together with the uniqueness of the lifted maps in the homotopy category, and
the two constructions agree up to the canonical commutativity constraint of
Lemma 15.60.14 of the Stacks Project, Tag
[0BYI](https://stacks.math.columbia.edu/tag/0BYI), which is functorial in
both complexes; hence the object is functorial in both variables at once.
