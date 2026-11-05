+++
id = "remark-properness-needed-c7"
kind = "remark"
title = "Why properness is needed in $(C_7)$"
name_showing = false
order = 366
uses = ["proposition-proper-base-change-projective-line"]
+++
Properness in $(C_7)$ is needed when the torsion order is divisible by
the characteristic, and this case arises in Proposition [proposition-proper-base-change-projective-line],
where the field is extended for arbitrary torsion sheaves. For example, in characteristic $p$,

$$
H^1(\mathbf A^1_k,\mathbf F_p)
=k[t]/\{h^p-h:h\in k[t]\},
$$

and extending an algebraically closed ground field adds new classes.
Indeed, we have $c^pt^{pm}\equiv ct^m$, and every element of $k$ is of the
form $h^p-h$. It follows that every class has a unique representative
$\sum_{p\nmid m}a_mt^m$, and the same holds over an algebraically closed
$k'\supset k$. Hence for $a\in k'\smallsetminus k$ the class of $at$ does
not come from $k[t]$.
