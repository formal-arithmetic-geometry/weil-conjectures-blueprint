+++
kind  = "proof"
of    = "lemma-openclosed-vanishing-lowershriek"
+++
The point of the argument is that no section of $j_!\mathcal G$ is computed:
$j_!$ is a sheafification and its sections are not accessible. Instead one
uses only adjunctions. For every $\mathcal H\in\shv{\et Z}$,

$$
\Hom(i^*j_!\mathcal G,\mathcal H)
\cong\Hom(j_!\mathcal G,i_*\mathcal H)
\cong\Hom(\mathcal G,j^*i_*\mathcal H)=0
$$

by [lemma-openclosed-vanishing-lowerstar]. Taking
$\mathcal H=i^*j_!\mathcal G$ shows that the identity of
$i^*j_!\mathcal G$ is zero, that is, $i^*j_!\mathcal G=0$.
