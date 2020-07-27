import xml.etree.ElementTree as ET

data = """<template id="solicitacao_form_pm" name="Formulário">
            <t t-call="website.layout">
                <div class="row">
                    <t t-call="syd_website.steps_process"/>
                </div>
                <div class="container">

                    <div class="content-group">
                        <span t-field="form.display_name"
                            t-options='{"fields": ["display_name"]}'/>
                        <span t-field="form.create_date" itemprop="create_date"/>
                    </div>
                </div>
            </t>
        </template>"""

myroot = ET.fromstring(data)

print(myroot.tag, myroot.attrib)

for x in myroot[0]:
    print(x.tag, x.attrib, x.text)

for x in myroot.findall('t'):
    print(x.attrib)