+++
kind  = "proof"
of    = "sk-lem-nagata-density-normalization"
uses = ["sk-prop-sf-open-closed-triangle"]
+++
The open and closed immersion operations on the pro-étale site are exact by
[sk-prop-sf-open-closed-triangle]. Its quasi-compact-open hypothesis applies
to the complement of $Z$ here because $\overline X$ is Noetherian, and
therefore ensures exactness of $i_*$. Extension by zero along $j$ is
supported on $X$, which lies in $Z$. Its inverse image on $Z$ is extension by
zero along $j_Z$. Equivalently, the natural map

$$
j_!K\longrightarrow i_*i^*j_!K=i_*j_{Z,!}K
$$

is the identity on the open $X$ and both sides restrict to zero on its closed
complement. The open–closed localization sequence therefore makes it an
isomorphism. Since the immersion operations are exact, the argument applies
degreewise to unbounded complexes.

Since $i_*$ is exact, $Ri_*=i_*$. The derived direct-image composition
isomorphism $Rp_*Ri_*\simeq R(p\circ i)_*$ proves the second
identification, as a composite of derived right adjoints.
