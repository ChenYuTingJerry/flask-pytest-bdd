from lxml import etree

from HelpServiceAPI.utils.converter import StringConverter


def parsing_response(xml_text, find_tag):
    root = etree.fromstring(xml_text)
    expr = "//*[local-name() = $name]"
    pvid_info = root.xpath(expr, name=find_tag)
    fail_info = root.xpath(expr, name="Fault")
    result = {}
    if len(pvid_info) > 0:
        result["status"] = "SUCCESS"
        result["data"] = {}
        for element in pvid_info[0]:
            result["data"][
                StringConverter.to_snake_case(element.tag[element.tag.index("}") + 1 :])
            ] = element.text
    elif len(fail_info) > 0:
        result["status"] = "FAILED"
        result["data"] = {}
        for element in fail_info[0]:
            result["data"][StringConverter.to_snake_case(element.tag)] = element.text
    return result


request_body_map = {
    "GetPVIDConfigInfoByPVID": lambda params: """
            <soapenv:Envelope 
                xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
                xmlns:tm="http://www.trendmicro.com/WSE/SOA" 
                xmlns:tren="http://TrendMicro.SOA5.SOAService.ServiceContracts">
               <soapenv:Header>
                   <tm:User>{auth_user}</tm:User>
                   <tm:AuthKey>{auth_key}</tm:AuthKey>
               </soapenv:Header>
               <soapenv:Body>
                  <tren:PVIDConfigInfoByPVIDRequest>
                     <!--Optional:-->
                     <tren:WebstoreProductID>{plan_id}</tren:WebstoreProductID>
                     <!--Optional:-->
                     <tren:WebstoreVersionID>{plan_id}</tren:WebstoreVersionID>
                  </tren:PVIDConfigInfoByPVIDRequest>
               </soapenv:Body>
            </soapenv:Envelope>
        """.format(
        **params
    ),
}
