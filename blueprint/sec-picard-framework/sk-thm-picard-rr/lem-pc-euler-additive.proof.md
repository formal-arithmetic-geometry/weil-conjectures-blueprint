+++
kind  = "proof"
of    = "lem-pc-euler-additive"
+++
The long exact cohomology sequence of the short exact sequence is

$$
0\to H^0(\mathcal{F}_1)\to H^0(\mathcal{F}_2)\to H^0(\mathcal{F}_3)\to H^1(\mathcal{F}_1)\to H^1(\mathcal{F}_2)
\to H^1(\mathcal{F}_3)\to\cdots,
$$

exact, terminates at both ends (finite support and finite
dimensionality of the terms, [lem-pc-coherent-hi] applied to the proper
structure morphism $X\to\operatorname{Spec}(k)$), and the
alternating sum of the dimensions in an exact sequence of finite
dimensional vector spaces vanishes (rank–nullity, applied inductively
to the decompositions $0\to\operatorname{im}\to V\to\operatorname{im}'\to0$). Summing the
alternative signs over the long exact sequence gives

$$
0=\sum_i(-1)^i\bigl(\dim H^i(\mathcal{F}_1)-\dim H^i(\mathcal{F}_2)+\dim H^i(\mathcal{F}_3)\bigr),
$$

which is exactly $\chi(\mathcal{F}_1)-\chi(\mathcal{F}_2)+\chi(\mathcal{F}_3)=0$, as claimed
(Varieties, Lemma 33.33.2, Tag
[08AA](https://stacks.math.columbia.edu/tag/08AA)).

