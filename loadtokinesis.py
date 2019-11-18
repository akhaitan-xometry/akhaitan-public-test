import lambdainit  # noqa: F401

import base64

import boto3

import config
import lambdalogging

LOG = lambdalogging.getLogger(__name__)
FIREHOSE = boto3.client('firehose')

def handler(event, context):
    """Forward JSON-formatted CW Log events to Firehose Delivery Stream."""
    #LOG.debug('Received event: %s', event)

    #log_messages = _get_log_messages(event)
    for x in range(10):
        time.sleep(1)
        FIREHOSE.put_record(
            DeliveryStreamName='ak-shipping',
            Record={                    
               'Data': datetime.now(tz)
                }
            )
