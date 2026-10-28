+++
kind = "proof"
of = "sk-thm-sf-pf-field"
uses = ["sk-lem-sf-determination", "sk-cor-coefficient-heart-ii", "sk-thm-sfb-proper-base-change"]
+++
Fixing all variables but one, the objects satisfying a claim form a localizing
subcategory, so it suffices that it contains $\Dbc$ ([sk-lem-sf-determination]). By the
dévissage of [sk-cor-coefficient-heart-ii], $\Dbc$ is closed under $\otimes^{\mathbf L}$,
since $a_!L\otimes^{\mathbf L}b_!M$ is the extension by zero of a lisse sheaf. The
projection formula on $\Dbc$ is [sk-thm-sfb-proper-base-change].
